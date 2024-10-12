# Text

The `Text` class allows you to draw and clear text on the canvas. You can specify the coordinates and content to be displayed.

## Installation

Ensure you have the `kandinsky` module available in your environment.

## Usage Example

```python
from canvas import Text

# Create text at (10, 10) with the content "Hello, World!"
text = Text(10, 10, "Hello, World!")

# Draw the text on the canvas
text.draw()

# Remove the text from the canvas
text.destroy()
