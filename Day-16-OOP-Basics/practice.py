# Practice Question 1

class Person:

    name = "John"

person1 = Person()

print(person1.name)

# Practice Question 2

class Animal:

    def sound(self):
        print("Animal makes a sound")

animal1 = Animal()

animal1.sound()

# Practice Question 3

class Laptop:

    brand = "Dell"

    def display(self):
        print("Brand:", self.brand)

laptop1 = Laptop()

laptop1.display()

# Practice Question 4

class Book:

    title = "Python Basics"

book1 = Book()

print(book1.title)

# Mini Task

class Employee:

    name = "Sam"
    department = "IT"

    def details(self):
        print("Name:", self.name)
        print("Department:", self.department)

employee1 = Employee()

employee1.details()
