# Creating a Class

class Student:

    name = "Sam"

    def greet(self):
        print("Hello,", self.name)

# Creating Object

student1 = Student()

print("Student Name:", student1.name)

student1.greet()

# Another Class

class Car:

    brand = "Toyota"

    def show_brand(self):
        print("Brand:", self.brand)

car1 = Car()

car1.show_brand()
