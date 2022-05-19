class Intern:
  def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
    self.name = name

obj = Intern()
obj.name = "Guido"
print(obj.name)