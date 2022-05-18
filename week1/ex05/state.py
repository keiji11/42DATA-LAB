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
