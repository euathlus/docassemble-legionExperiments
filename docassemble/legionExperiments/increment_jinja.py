# pre-load
from docassemble.base.util import register_jinja_filter

def increment(num):
  
  return float(num) + 1

register_jinja_filter('increment', increment)