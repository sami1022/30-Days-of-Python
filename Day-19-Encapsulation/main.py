# Encapsulation Example

class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

student = Student("Sam", 20)

print("Name:", student.name)

print("Age:", student.get_age())

student.set_age(21)

print("Updated Age:", student.get_age())
