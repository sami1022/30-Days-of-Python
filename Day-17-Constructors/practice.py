# Practice Question 1

class Employee:

    def __init__(self, name):
        self.name = name

employee1 = Employee("John")

print(employee1.name)

# Practice Question 2

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Python Basics", "ABC")

print(book1.title)
print(book1.author)

# Practice Question 3

class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

mobile1 = Mobile("Samsung", 25000)

mobile1.display()

# Mini Task

class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def details(self):
        print("Name:", self.name)
        print("Course:", self.course)

student1 = Student("Sam", "Python")

student1.details()
