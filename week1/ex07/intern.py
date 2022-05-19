class Coffee:
  def __str__(self):
    return "This is the worst coffee you ever tasted."

class Intern(Coffee):
  def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
    self.name = name
  def __str__(self):
    return self.name

def make_coffee(intern):
  return Coffee()
def work(e):
  raise Exception("I’m just an intern, I can’t do that...")

intern1 = Intern()
intern2 = Intern("Mark")
try:
  print(intern1.__str__())
  print(intern2.__str__())
  print(intern2.name,", may I have a coffee please?")
  print(make_coffee(intern1))
  print("May I have some work here please?")
  print(work(intern2))
except Exception as e:
  print(e)