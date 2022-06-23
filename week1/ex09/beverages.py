from textwrap import dedent

class HotBeverage:
  def __init__(self, name="hot beverage", price=0.3):
      self.name = name
      self.price = price
  
  def description(self):
      return "Just some hot water in a cup."
  
  def __str__(self):
      return dedent(f'''
                name : {self.name} 
                price : {format(self.price, ".2f")}
                description : {self.description()}''')

class Coffee(HotBeverage):
  def __init__(self, name="coffee", price=0.4):
      super().__init__(name, price)
  
  def description(self):
      return "A coffee, to stay awake."

class Tea(HotBeverage):
  def __init__(self, name="tea", price=0.3):
      super().__init__(name, price)

class Chocolate(HotBeverage):
  def __init__(self, name="chocolate", price=0.5):
      super().__init__(name, price)
  
  def description(self):
      return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
  def __init__(self, name="cappuccino", price=0.45):
      super().__init__(name, price)
  
  def description(self):
      return "Un po' di Italia nella sua tazza!"
                
# print(HotBeverage())
# print(Coffee())
# print(Tea())
# print(Chocolate())
# print(Cappuccino())