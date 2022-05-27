from colorama import init, Fore, Back, Style

# Initializes Colorama
init(autoreset=True)

from beverages import *
import random
import os
import time
  
class EmptyCup(HotBeverage):
	def __init__(self, name="empty cup", price=0.9):
		self.name = name
		self.price = price
	def description(self):
		return Fore.MAGENTA + "An empty cup?! Gimme my money back!"

class CoffeeMachine:
	def __init__(self):
		self.drinks = 0
		self.broke = False

	def repair(self):
		self.drinks = 0
		self.broke = False
		print(Fore.GREEN + "The coffee machine has been repaired.")

	def serve(self, beverage):
		if self.drinks >= 2:
			self.broke = True
			raise BrokenMachineException
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

class BrokenMachineException(Exception):
	def __init__(self):
		print(Fore.RED + "This coffee machine has to be repaired.")

c = CoffeeMachine()
beveragesList = ["tea", "coffee", "cappuccino", "chocolate", "empty cup"]
while True:
	try:
		print("What do you want to drink?")
		item = random.choice(beveragesList)
		print("YOUR CHOICE IS = " + Fore.LIGHTGREEN_EX + item)
		print(c.serve(item))
		if (item != "empty cup"):
			print(Fore.CYAN + "Waiting...")
			time.sleep(3)
	except:
		print("In repair...waiting...")
		time.sleep(5)
		c.repair()
	print("")
	if (item != "empty cup" and c.drinks != 0):
		print(Fore.YELLOW + "Drink #" + str(c.drinks) + " served!")
	print("-----------------------------------------------------")
	print("Type 'y' to exit the program.")
	print("Type something else to continue the program.\n")
	choose = input("Do you want to exit?(y/n)\n")
	if choose == "y":
		break
	else:
		continue


os.system('python3 beverages.py')
# os.system('python3 multiple.py')
