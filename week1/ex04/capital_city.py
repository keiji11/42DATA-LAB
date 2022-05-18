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
