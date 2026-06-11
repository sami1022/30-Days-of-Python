# Practice Question 1

class Person:

    def introduce(self):
        print("I am a Person")

class Student(Person):
    pass

student = Student()

student.introduce()

# Practice Question 2

class Animal:

    def eat(self):
        print("Animal Eats")

class Cat(Animal):

    def meow(self):
        print("Cat Meows")

cat = Cat()

cat.eat()
cat.meow()

# Practice Question 3

class Employee:

    def work(self):
        print("Employee Working")

class Manager(Employee):

    def manage(self):
        print("Managing Team")

manager = Manager()

manager.work()
manager.manage()

# Mini Task

class Shape:

    def display(self):
        print("This is a Shape")

class Circle(Shape):

    def area(self):
        print("Area = πr²")

circle = Circle()

circle.display()
circle.area()
