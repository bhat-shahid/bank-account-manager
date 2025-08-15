class Person:
    def __init__(self, name, age):
        self.name = name
        self.age=age
    def display(self):
        print(f"Name is {self.name} and age is {self.age}")
class Student(Person):
    def __init__(self, name, age, grade=None):
        super().__init__(name, age)
        self.grade = grade
    def calculate_result(self,marks_list):
        average=sum(marks_list)/len(marks_list)
        if average>=90:
            self.grade="A"
        elif average>=75 and average<=89:
            self.grade="B"
        elif average>=50 and average<=74:
            self.grade="C"
        else:
            self.grade="D"
    def display(self):
        super().display()
        print(f"grade is {self.grade}")
class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
    def increase_salary(self,amount):
        self.salary+=amount
    def display(self):
        super().display()
        print(f"subject is {self.subject}, salary is {self.salary}")
s1 = Student("Ali", 20)
t1 = Teacher("Sara", 35, "Math", 50000)
s1.calculate_result([80, 90, 85])
t1.increase_salary(5000)
s1.display()
t1.display()