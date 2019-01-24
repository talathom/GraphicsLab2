import math
class Circle:
	def __init__(self, radius):
		self.radius = radius
		
	def getArea(self):
		return math.pi * math.pow(self.radius, 2)
		
	def getPerimeter(self):
		return 2 * math.pi * self.radius
		
	def toString(self):
		return "Circle with radius "+ str(self.radius) +"\nArea: " + str(self.getArea()) +"\nPerimeter: " + str(self.getPerimeter())
		
		
class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
	def getArea(self):
		return self.width * self.height
		
	def getPerimeter(self):
		return 2 * self.width + 2 * self.height
		
	def toString(self):
		return "Rectangle with width "+ str(self.width)+ " and height "+ str(self.height)+ "\nArea: " + str(self.getArea()) +"\nPerimeter: " + str(self.getPerimeter())
		
c1 = Circle(5)
r1 = Rectangle(3,2)
c2 = Circle(3)
c3 = Circle(1)
r2 = Rectangle(1,1)

listShapes = [c1,r1,c2,c3,r2]
for shape in listShapes:
	print(shape.toString())