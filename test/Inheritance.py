class Animal:
    def speak(self):
        print("Animals make sound")

class Dog(Animal):      # Dog inherits from Animal
    def speak(self):    # Overriding method
        print("Dog barks 🐶")

dog = Dog()
dog.speak()
