from abc import ABC, abstractmethod

# Practice Question 1

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def area(self):
        print("Area of Circle")

circle = Circle()

circle.area()

# Practice Question 2

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car Started")

car = Car()

car.start()

# Practice Question 3

class Employee(ABC):

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):

    def work(self):
        print("Writing Code")

developer = Developer()

developer.work()

# Mini Task

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):

    def pay(self):
        print("Payment via UPI")

upi = UPI()

upi.pay()
