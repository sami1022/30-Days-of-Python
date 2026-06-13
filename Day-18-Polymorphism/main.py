# Polymorphism Example

class Animal:

    def sound(self):
        print("Animal makes a sound")

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

# Another Example

class Bird:

    def move(self):
        print("Bird is Flying")

class Fish:

    def move(self):
        print("Fish is Swimming")

bird = Bird()
fish = Fish()

bird.move()
fish.move()
