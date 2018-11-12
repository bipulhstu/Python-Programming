class Vehicle:
	"""Base class for all vehicles"""
	def __init__(self, name, manufacturer, color):
		self.name = name
		self.manufacturer = manufacturer
		self.color = color

	def drive(self):
		print("Driving", self.manufacturer, self.name)

	def turn(self, direction):
		print("Turning", self.name, " to ", direction)

	def brake(self):
		print(self.name, " is stopping!!")

class Car(Vehicle):
	"""Car Class"""

	def change_gear(self, gear_name):
		"""method for printing gear"""
		print(self.name, " is changing gear to ", gear_name)

if __name__ == '__main__':
	v1 = Vehicle("Fusion 110 EX", "Walton", "Black")

	v1.drive()

	v1.turn("left")

	v1.change_gear("P")

	v1.brake()

