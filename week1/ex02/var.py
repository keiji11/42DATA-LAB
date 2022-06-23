""" 
Create a script named "var.py" in which you will define a
my_var function. In this function, you will declare 9
variables of different types and print them on the
standard output. You will reproduce this output exactly:

$> python3 var.py
42 has a type <class 'int'>
42 has a type <class 'str'>
quarante-deux has a type <class 'str'>
42.0 has a type <class 'float'>
True has a type <class 'bool'>
[42] has a type <class 'list'>
{42: 42} has a type <class 'dict'>
(42,) has a type <class 'tuple'>
set() has a type <class 'set'>
$>
"""
def ft_print(x):
  print(x, "has a type", type(x))

def my_var():
  y=42
  ft_print(y)
  y="42"
  ft_print(y)
  y="quarante-deux"
  ft_print(y)
  y=42.0
  ft_print(y)
  y=True
  ft_print(y)
  y=[42]
  ft_print(y)
  y={42:42}
  ft_print(y)
  y=(42,)
  ft_print(y)
  y=set()
  ft_print(y)

my_var()