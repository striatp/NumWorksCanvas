# Rectangle

The `Rectangle` class enables the creation and manipulation of rectangles on the canvas. You can draw rectangles with specified coordinates, dimensions, and colors.

## Installation

Ensure you have the `kandinsky` module available in your environment.

## Usage Example

```python
from canvas import Rectangle

# Create a rectangle at (50, 50) with a width of 100, height of 50, and blue color
rectangle = Rectangle(50, 50, 100, 50, "blue")

# Draw the rectangle on the canvas
rectangle.draw()

# Remove the rectangle from the canvas
rectangle.destroy()
