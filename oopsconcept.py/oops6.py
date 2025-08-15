class Vehicle:
    def __init__(self,brand, color, year):
        self.brand = brand
        self.color = color
        self.year=year
    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Year: {self.year}")
class Truck(Vehicle):
    def __init__(self, brand, color, year, load_capacity):
        super().__init__(brand, color, year)
        self.load_capacity=load_capacity
    def display(self):
        super().display()
        print(f"load_capacity: {self.load_capacity}")
car1=Truck("Tata", "White", 2018, 15)
car1.display()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age=age
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade=grade
    def display(self):
        super().display()
        print(f"Grade: {self.grade}")
student1=Student("Rohan", 16, "10th")
student1.display()