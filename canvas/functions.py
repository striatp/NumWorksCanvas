import math
import kandinsky

# Initialization error
class InitError(Exception):
    """Exception raised when attempting to draw on an uninitialized canvas."""
    pass

# Missing argument error
class MissingArgumentError(Exception):
    """Exception raised for missing or invalid arguments."""
    pass

# Variables used to track the canvas' data
canvas_initialized = False
default_bg_color = "white"

# Initialization of the canvas
class Canvas:
    # Initializing
    def __init__(self, background_color: str or tuple = default_bg_color) -> None:
        global canvas_initialized

        # Check if the canvas is already initialized
        if canvas_initialized:
            raise InitError("The canvas is already initialized.")
        
        # Validate background_color
        valid_colors = {"red", "green", "yellow", "blue", "brown", "black", "white", "pink", "orange", "purple", "gray"}
        
        if isinstance(background_color, str):
            if background_color not in valid_colors:
                raise ValueError("The 'background_color' must be a valid color.")
        elif isinstance(background_color, tuple):
            if len(background_color) != 3 or not all(isinstance(c, int) and 0 <= c <= 255 for c in background_color):
                raise ValueError("The 'background_color' tuple must contain three integers between 0 and 255 (e.g., (255, 255, 255)).")
        else:
            raise TypeError("The 'background_color' argument must be a string (color name) or a tuple (RGB values).")

        # Set canvas attributes
        self.background_color = background_color

        # Mark canvas as initialized
        canvas_initialized = True

        # Initialize the canvas on the screen
        self.create_canvas()

    # Method to create the canvas and display it on the screen
    def create_canvas(self) -> None:
        """Creates the canvas on the screen with the specified background color."""

        # Fill the canvas with the background color
        if isinstance(self.background_color, str):
            color = self.get_color_tuple(self.background_color)
        else:
            color = self.background_color

        kandinsky.fill_rect(0, 0, 320, 222, self.background_color)

    @staticmethod
    def get_color_tuple(color_name: str) -> tuple:
        """Returns the RGB tuple corresponding to a color name."""
        color_map = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "yellow": (255, 255, 0),
            "blue": (0, 0, 255),
            "brown": (165, 42, 42),
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "pink": (255, 192, 203),
            "orange": (255, 165, 0),
            "purple": (128, 0, 128),
            "gray": (128, 128, 128)
        }
        return color_map.get(color_name, (255, 255, 255))  # Default to white

# Circle function
class Circle:
    def __init__(self, x: int, y: int, radius: int, color: str or tuple) -> None:
        global canvas_initialized

        # Checks if the canvas is initialized
        if not canvas_initialized:
            raise InitError("The canvas is not initialized.")
        
        """Initialize the circle with center, radius, and color."""
        # Validate position and radius
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Coordinates 'x' and 'y' must be integers.")
        if not isinstance(radius, int) or radius <= 0:
            raise ValueError("Radius must be a positive integer.")

        # Validate color
        valid_colors = {"red", "green", "yellow", "blue", "brown", "black", "white", "pink", "orange", "purple", "gray"}
        if isinstance(color, str):
            if color not in valid_colors:
                raise ValueError("The color must be one of the following: " + ", ".join(valid_colors))
        elif isinstance(color, tuple):
            if len(color) != 3 or not all(isinstance(c, int) and 0 <= c <= 255 for c in color):
                raise ValueError("Color tuple must contain three integers between 0 and 255.")
        else:
            raise TypeError("Color must be a string (color name) or a tuple (RGB values).")

        # Set circle attributes
        self.x = x
        self.y = y
        self.radius = radius
        self.color = self.get_color_tuple(color) if isinstance(color, str) else color
        self.is_drawn = False  # Track if the circle is drawn

    def draw(self) -> None:
        """Draw the circle on the canvas."""
        if self.is_drawn:
            raise InitError("The circle is already drawn.")

        # Draw the circle using kandinsky.set_pixel and a simple algorithm
        for angle in range(0, 360):
            for r in range(self.radius):
                x_offset = int(r * math.cos(math.radians(angle)))
                y_offset = int(r * math.sin(math.radians(angle)))
                kandinsky.set_pixel(self.x + x_offset, self.y + y_offset, self.color)

        self.is_drawn = True

    def destroy(self) -> None:
        """Remove the circle by filling the area with the background color."""
        if not self.is_drawn:
            raise InitError("The circle is not drawn yet.")
        
        background_color = (255, 255, 255)  # Default background color (white)
        for angle in range(0, 360):
            for r in range(self.radius):
                x_offset = int(r * math.cos(math.radians(angle)))
                y_offset = int(r * math.sin(math.radians(angle)))
                kandinsky.set_pixel(self.x + x_offset, self.y + y_offset, background_color)

        self.is_drawn = False

    @staticmethod
    def get_color_tuple(color_name) -> tuple:
        """Return the RGB tuple for a color name."""
        color_map = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "yellow": (255, 255, 0),
            "blue": (0, 0, 255),
            "brown": (165, 42, 42),
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "pink": (255, 192, 203),
            "orange": (255, 165, 0),
            "purple": (128, 0, 128),
            "gray": (128, 128, 128)
        }
        return color_map.get(color_name, (255, 255, 255))  # Default to white if color not found

# Rectangle function
class Rectangle:
    def __init__(self, x: int, y: int, width: int, height: int, color: str or tuple):
        global canvas_initialized

        # Checks if the canvas is initialized
        if not canvas_initialized:
            raise InitError("The canvas is not initialized.")
        
        """Initialize the rectangle with width, height and color."""
        # Initialize the rectangle's attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = self.get_color_tuple(color)
        self.is_drawn = False  # To keep track if the rectangle is drawn

    def draw(self):
        """Draws the rectangle on the screen."""
        if not self.is_drawn:
            kandinsky.fill_rect(self.x, self.y, self.width, self.height, self.color)
            self.is_drawn = True

    def destroy(self):
        """Removes the rectangle by filling it with white (default background)."""
        if self.is_drawn:
            kandinsky.fill_rect(self.x, self.y, self.width, self.height, (255, 255, 255))  # Fill with white to "erase"
            self.is_drawn = False

    @staticmethod
    def get_color_tuple(color_name: str or tuple) -> tuple:
        """Converts a color name or tuple into an RGB tuple."""
        if isinstance(color_name, tuple):
            return color_name
        color_map = {
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "yellow": (255, 255, 0),
            "blue": (0, 0, 255),
            "brown": (165, 42, 42),
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "pink": (255, 192, 203),
            "orange": (255, 165, 0),
            "purple": (128, 0, 128),
            "gray": (128, 128, 128)
        }
        return color_map.get(color_name, (255, 255, 255))  # Default to white

# Text function
class Text:
    def __init__(self, x: int, y: int, content: str) -> None:
        # Initialize text attributes
        self.x = x
        self.y = y
        self.content = content
        self.is_drawn = False  # To track if the text is displayed

    def draw(self):
        """Draws the text on the screen."""
        if not self.is_drawn:
            kandinsky.draw_string(self.content, self.x, self.y)
            self.is_drawn = True

    def destroy(self):
        """Clears the text by filling the area where it was drawn with the default background color."""
        if self.is_drawn:
            # Calculate the size of the text based on its length (assuming a fixed-width font)
            text_width = len(self.content) * 10  # NumWorks uses 10x10 font size
            text_height = 15

            # Overwrite the text area with the default background color (white)
            kandinsky.fill_rect(self.x, self.y, text_width, text_height, (255, 255, 255))  # White background
            self.is_drawn = False

# Triangle function
class Triangle:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
        # Initialize triangle vertices
        self.vertices = [(x1, y1), (x2, y2), (x3, y3)]
        self.is_drawn = False  # To track if the triangle is displayed

    def draw(self):
        """Draws the triangle on the screen using kandinsky."""
        if not self.is_drawn:
            self.fill_triangle(self.vertices[0], self.vertices[1], self.vertices[2])
            self.is_drawn = True

    def fill_triangle(self, v1, v2, v3):
        """Fills the triangle defined by vertices v1, v2, v3."""
        # Get the vertices
        x1, y1 = v1
        x2, y2 = v2
        x3, y3 = v3
        
        # Sort the vertices by y-coordinate
        vertices = sorted([v1, v2, v3], key=lambda v: v[1])
        (x1, y1), (x2, y2), (x3, y3) = vertices

        # Draw the triangle by filling pixels
        for y in range(y1, y3 + 1):
            if y < y2:
                # Calculate the x coordinates for the left and right edges
                x_left = self.interpolate(x1, y1, x2, y2, y)
                x_right = self.interpolate(x1, y1, x3, y3, y)
            else:
                # For the bottom part of the triangle
                x_left = self.interpolate(x2, y2, x3, y3, y)
                x_right = self.interpolate(x1, y1, x3, y3, y)
                
            # Fill the line between left and right
            for x in range(int(x_left), int(x_right) + 1):
                kandinsky.set_pixel(x, y, (0, 0, 0))  # Fill with black

    def interpolate(self, x1, y1, x2, y2, y):
        """Interpolates x-coordinate based on the y-coordinate between two points."""
        if y2 == y1:
            return x1
        return x1 + (x2 - x1) * (y - y1) // (y2 - y1)

    def destroy(self):
        """Clears the triangle by filling the area where it was drawn with the default background color."""
        if self.is_drawn:
            # Overwrite the triangle area with the default background color (white)
            self.fill_triangle(self.vertices[0], self.vertices[1], self.vertices[2], fill=False)
            self.is_drawn = False

    def fill_triangle(self, v1, v2, v3, fill=True):
        """Fills the triangle defined by vertices v1, v2, v3, with the background color if fill is False."""
        # Get the vertices
        x1, y1 = v1
        x2, y2 = v2
        x3, y3 = v3
        
        # Sort the vertices by y-coordinate
        vertices = sorted([v1, v2, v3], key=lambda v: v[1])
        (x1, y1), (x2, y2), (x3, y3) = vertices

        # Draw the triangle by filling pixels
        for y in range(y1, y3 + 1):
            if y < y2:
                x_left = self.interpolate(x1, y1, x2, y2, y)
                x_right = self.interpolate(x1, y1, x3, y3, y)
            else:
                x_left = self.interpolate(x2, y2, x3, y3, y)
                x_right = self.interpolate(x1, y1, x3, y3, y)

            for x in range(int(x_left), int(x_right) + 1):
                # Fill with black if filling, else fill with the default background color
                color = (255, 255, 255) if not fill else (0, 0, 0)
                kandinsky.set_pixel(x, y, color) 
