import inspect

## add function present in python_functions.py file
def add(x, y):
  return x + y
## you want to inspect it in analysis.py file
print(inspect.getsource(add))