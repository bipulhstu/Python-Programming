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


if __name__ == '__main__':
	v1 = Vehicle("Fusion 110 EX", "Walton", "Black")
	v2 = Vehicle("Softail Delux", "Harley-Davidson", "Blue")

	v1.drive()
	v2.drive()

	v1.turn("left")
	v2.turn("right")

	v1.brake()
	v2.brake()

