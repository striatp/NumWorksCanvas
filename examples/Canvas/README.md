# Canvas

The `Canvas` class is the foundational component for creating a drawable area on the NumWorks calculator screen. It allows you to initialize a canvas with a specified background color and ensures that only one instance can be created.

## Installation

Ensure you have the `kandinsky` module available in your environment.

## Usage Example

```python
from canvas import Canvas

# Create a canvas with a blue background
# The 'background_color' argument is optional
# Not implementing it will initiate a white canvas
canvas = Canvas(background_color="blue")
```
