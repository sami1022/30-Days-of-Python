# Parent Class

class Animal:

    def sound(self):
        print("Animal makes a sound")

# Child Class

class Dog(Animal):

    def bark(self):
        print("Dog barks")

dog = Dog()

dog.sound()
dog.bark()

# Another Example

class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):

    def drive(self):
        print("Car is Driving")

car = Car()

car.start()
car.drive()
