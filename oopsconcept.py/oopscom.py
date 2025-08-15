# # class Camera:
# #     def take_photo(self):
# #         print("Photo taken!")
# # class Smartphone:
# #     def __init__(self):
# #         self.Camera=Camera()
# #     def use_camera(self):
# #         self.Camera.take_photo()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}, aged {self.age}"

#     def __repr__(self):
#         return f"Person(name='{self.name}', age={self.age})"

# p = Person("Ali", 30)
# print(p)        # Calls __str__ → Ali, aged 30
# print(repr(p))  # Calls __repr__ → Person(name='Ali', age=30)
class Person:
    def __init__(self, name):
        self.name = name

    def fgh(self):
        return f"My name is {self.name}"

p = Person("Ali")
print(p)
