"""
Write a program that prints the sum of two numbers inserted by the user.
"""
import sys

try:
  if len(sys.argv) != 3:
    raise ValueError("Invalid number of arguments")
  else:
    print(float(sys.argv[1]) + float(sys.argv[2]))
except ValueError as e:
  print(e)
  print("Usage: ./print_sum.py <number1> <number2>")
  sys.exit(1)

