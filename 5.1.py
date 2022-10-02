import math


class Rectangle:

    def __init__(self, color="green", width=100, height=100):
        self.color = color
        self.width = width
        self.height = height

        self.diagonal = math.sqrt(math.pow(self.height, 2) + math.pow(self.width, 2))

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * (self.width + self.height))


rectangle1 = Rectangle()
print(rectangle1.color)
print(rectangle1.diagonal)
print(rectangle1.square())
print(rectangle1.perimeter())

rectangle2 = Rectangle("yellow", 23, 34)
print(rectangle2.color)
print(rectangel2.diagonal)

print(rectangle2.square())
print(rectangle2.perimeter())
