"""
Write a program that lets the user insert a number of
hours, minutes and seconds and prints the total number of
seconds.
"""
import sys

print("Usage: ./print_secs.py <hour> ?<minute> ?<second>")
try:
  if (len(sys.argv) > 4) or (len(sys.argv) < 2):
    raise ValueError("Invalid number of arguments")
  else:
    if len(sys.argv) >= 2:
      ret = int(sys.argv[1]) * 60 * 60
    if len(sys.argv) >= 3:
      ret += int(sys.argv[2]) * 60
    if len(sys.argv) == 4:
      ret += int(sys.argv[3])
    print("Total number of seconds:", ret)
except ValueError as e:
  print(e)
  print("Usage: ./print_secs.py <hour> ?<minute> ?<second>")
  sys.exit(1)