from abc import ABC, abstractmethod

# Abstract Class

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

# Child Class

class Dog(Animal):

    def sound(self):
        print("Dog Barks")

class Cat(Animal):

    def sound(self):
        print("Cat Meows")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
