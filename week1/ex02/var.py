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