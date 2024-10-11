import kandinsky

# Initialization error
class InitError(Exception):
  """Raised exception for initialization issues : the canvas must be initialized before adding drawings."""
  pass

# Missing argument error
class MissingArgumentError(Exception):
  """Raised exception for missing arguments or invalid type input."""
  pass
