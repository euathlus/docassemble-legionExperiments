# pre-load
from docassemble.base.util import register_jinja_filter

def multiply_triple_jinja(a, b, c):
  """Adds three numbers together.

  Args:
    a: The first number.
    b: The second number.
    c: The third number.

  Returns:
    The sum of the three numbers.
  """
  
  return float(a) * float(b) * float(c)

register_jinja_filter('multiply_triple_jinja', multiply_triple_jinja)