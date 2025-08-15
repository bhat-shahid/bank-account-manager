import math
class Shape:
        def get_area(self):
            print("Area not defined")
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):
        print(f" Area of circle{math.pi * (self.radius ** 2)}")
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth=breadth
    def get_area(self):
        print(f"Area of rectangle{self.length * self.breadth}")
shapes = [
    Circle(5),
    Rectangle(4, 6)
]

for shape in shapes:
    shape.get_area()


