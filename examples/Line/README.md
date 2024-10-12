# Line

The `Line` class allows you to draw and clear lines on the canvas. It utilizes Bresenham's line algorithm for precise rendering.

## Installation

Ensure you have the `kandinsky` module available in your environment.

## Usage Example

```python
from canvas import Line

# Create a line from (10, 10) to (100, 100)
line = Line(10, 10, 100, 100)

# Draw the line on the canvas
line.draw()

# Remove the line from the canvas
line.destroy()
