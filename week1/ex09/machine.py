from beverages import *
import random
import os
import time
  
class EmptyCup(HotBeverage):
	def __init__(self, name="empty cup", price=0.9):
		self.name = name
		self.price = price
	def description(self):
		return "An empty cup?! Gimme my money back!"

class CoffeeMachine:
	def __init__(self):
		self.drinks = 0
		self.broke = False

	def repair(self):
		self.drinks = 0
		self.broke = False
		print("The coffee machine has been repaired.")

	def serve(self, beverage):
		if self.drinks >= 10:
			self.broke = True
			raise BrokenMachineException()
		if not self.broke:
			tea = Tea()
			coffee = Coffee()
			cappuccino = Cappuccino()
			chocolate = Chocolate()
			emptyCup = EmptyCup()
			if beverage == "tea":
				self.drinks+=1
				return tea
			elif beverage == "coffee":
				self.drinks+=1
				return coffee
			elif beverage == "cappuccino":
				self.drinks+=1
				return cappuccino
			elif beverage == "chocolate":
				self.drinks+=1
				return chocolate
			elif beverage == "empty cup":
				return emptyCup

class BrokenMachineException(Exception, CoffeeMachine):
	def __init__(self):
		print("This coffee machine has to be repaired.")
		print("Machine is broken...it will repair soon...")
		time.sleep(3)
		CoffeeMachine.repair(self)

c = CoffeeMachine()
beveragesList = ["tea", "coffee", "cappuccino", "chocolate", "empty cup"]
while True:
	print("What do you want to drink?")
	item = random.choice(beveragesList)
	print(item)
	print(c.serve(item))
	print("")
	print("Drink #" + str(c.drinks) + " served!\n")
	print("Type 'y' to exit the program.")
	print("Type something else to continue the program.\n")
	choose = input("Do you want to exit?(y/n)\n")
	if choose == "y":
		break
	else:
		continue


os.system('python3 beverages.py')
# os.system('python3 multiple.py')
