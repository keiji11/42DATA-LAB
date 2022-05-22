class CoffeeMachine:
	def __init__(self):
		pass

	class EmptyCup(HotBeverage):
		def __init__(self, name="empty cup", price=0.9):
			super().__init__(name, price)

		def description(self):
			return "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self, message="This coffee machine has to be repaired."):
			self.message = message
	
	def repair(self):
		pass

	def serve(self, beverage):
		beverage
		