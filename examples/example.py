import canvas as c

# Create the canvas
c.Canvas()

# Create a rectangle and draw it
rect = c.Rectangle(10, 10, 50, 80, (255, 100, 100))
rect.draw()

# Create a triangle and draw it
triangle = c.Triangle(75, 10, 125, 50, 150, 10)
triangle.draw()

# Create a circle and draw it
circle = c.Circle(150, 120, 50, "blue")
circle.draw()

# Create a line and draw it
line = c.Line(200, 50, 250, 150)
line.draw()

# Create a text and display it
text = c.Text(50, 190, "Hello, World!")
text.draw()
