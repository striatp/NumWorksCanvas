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
    def __init__(self, width: int or str, height: int or str, background_color: str or tuple = default_bg_color) -> None:
        global canvas_initialized

        # Check if the canvas is already initialized
        if canvas_initialized:
            raise InitError("The canvas is already initialized.")
        
        # Validate width
        if isinstance(width, str):
            if width != "full":
                raise ValueError("The 'width' argument must be a positive integer or the string 'full'.")
        elif isinstance(width, int):
            if width <= 0:
                raise ValueError("The 'width' argument must be a positive integer.")
        else:
            raise TypeError("The 'width' argument must be either an integer or a string ('full').")

        # Validate height (follows same structure as width validation)
        if isinstance(height, str):
            if height != "full":
                raise ValueError("The 'height' argument must be a positive integer or the string 'full'.")
        elif isinstance(height, int):
            if height <= 0:
                raise ValueError("The 'height' argument must be a positive integer.")
        else:
            raise TypeError("The 'height' argument must be either an integer or a string ('full').")

        # Validate background_color
        valid_colors = {"red", "green", "yellow", "blue", "brown", "black", "white", "pink", "orange", "purple", "gray"}
        
        if isinstance(background_color, str):
            if background_color not in valid_colors:
                raise ValueError(f"The 'background_color' must be one of the following: {', '.join(valid_colors)}.")
        elif isinstance(background_color, tuple):
            if len(background_color) != 3 or not all(isinstance(c, int) and 0 <= c <= 255 for c in background_color):
                raise ValueError("The 'background_color' tuple must contain three integers between 0 and 255 (e.g., (255, 255, 255)).")
        else:
            raise TypeError("The 'background_color' argument must be a string (color name) or a tuple (RGB values).")

        # Set canvas attributes
        self.width = width
        self.height = height
        self.background_color = background_color

        # Mark canvas as initialized
        canvas_initialized = True

        # Initialize the canvas on the screen
        self.create_canvas()

    def create_canvas(self):
        """Creates the canvas on the screen with the specified background color."""
        # Determine actual width and height if 'full' is specified
        if self.width == "full":
            self.width = 320
        if self.height == "full":
            self.height = 222

        # Fill the canvas with the background color
        if isinstance(self.background_color, str):
            color = self.get_color_tuple(self.background_color)
        else:
            color = self.background_color

        for x in range(self.width):
            for y in range(self.height):
                kandinsky.set_pixel(x, y, color)

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
