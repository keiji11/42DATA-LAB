"""
Re-using the same dictionaries from the previous
exercise, create a program that takes the capital city
for argument and displays the matching state this time.
The rest of your program’s behaviors must remain the same
as in the previous exercise.

$> python3 capital_city.py Oregon
Salem
$> python3 capital_city.py Ile-De-France
Unknown state
$> python3 capital_city.py
$> python3 capital_city.py Oregon Alabama
$> python3 capital_city.py Oregon Alabama Ile-De-France
$>
$> python3 state.py Salem
Oregon
$> python3 state.py Paris
Unknown capital city
$> python3 state.py
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
  if sys.argv[1] in capital_cities.values():
    key = [k for k, v in capital_cities.items() if v == sys.argv[1]]
    final_key = [k for k, v in states.items() if v == key[0]]
    print(final_key[0])
  else:
    print("Unknown state")
else:
  sys.exit()
