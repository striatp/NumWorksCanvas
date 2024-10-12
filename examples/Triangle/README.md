# Triangle

The `Triangle` class enables the creation and manipulation of triangles on the canvas. You can draw triangles defined by three vertices.

## Installation

Ensure you have the `kandinsky` module available in your environment.

## Usage Example

```python
from canvas import Triangle

# Create a triangle with vertices at (10, 10), (50, 50), and (100, 10)
triangle = Triangle(10, 10, 50, 50, 100, 10)

# Draw the triangle on the canvas
triangle.draw()

# Remove the triangle from the canvas
triangle.destroy()
