"""
Write a program that takes a state as an argument (ex:
Oregon) and displays its capital city (ex: Salem) on the
standard output. If the argument doesn’t give any result,
your script must display: Unknown state. If there is no
argument - or too many - your script must no do anything
and quit.

Dictionaries to copy unaltered:
states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

$> python3 capital_city.py Oregon
Salem
$> python3 capital_city.py Ile-De-France
Unknown state
$> python3 capital_city.py
$> python3 capital_city.py Oregon Alabama
$> python3 capital_city.py Oregon Alabama Ile-De-France
$>
"""

import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

if len(sys.argv) == 2:
  if sys.argv[1] in states:
    print(capital_cities[states[sys.argv[1]]])
  else:
    print("Unknown state")
else:
  sys.exit()
