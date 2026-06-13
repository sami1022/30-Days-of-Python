# Practice Question 1

class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):

    def start(self):
        print("Car Started")

car = Car()

car.start()

# Practice Question 2

class Employee:

    def work(self):
        print("Employee Working")

class Manager(Employee):

    def work(self):
        print("Manager Managing Team")

manager = Manager()

manager.work()

# Practice Question 3

class Shape:

    def area(self):
        print("Calculating Area")

class Circle(Shape):

    def area(self):
        print("Area of Circle")

circle = Circle()

circle.area()

# Mini Task

class Payment:

    def pay(self):
        print("Processing Payment")

class CreditCard(Payment):

    def pay(self):
        print("Payment via Credit Card")

class UPI(Payment):

    def pay(self):
        print("Payment via UPI")

credit = CreditCard()
upi = UPI()

credit.pay()
upi.pay()
