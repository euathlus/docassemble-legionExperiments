# pre-load
from docassemble.base.util import register_jinja_filter

def say_hello():
  """Adds three numbers together.

  Args:
    a: The first number.
    b: The second number.
    c: The third number.

  Returns:
    The sum of the three numbers.
  """
  
  return "Hello there!"

register_jinja_filter('say_hello', say_hello)