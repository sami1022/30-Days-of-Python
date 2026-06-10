# Constructor Example

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

student1 = Student("Sam", 20)

student1.display()

# Another Example

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car1 = Car("Toyota", "Camry")

car1.details()
