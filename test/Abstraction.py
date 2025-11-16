from abc import ABC, abstractmethod

class Vehicle(ABC):   # Abstract base class
    @abstractmethod
    def start_engine(self):
        pass           # Must be implemented in child class

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started 🚗")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started 🏍️")

car = Car()
car.start_engine()

bike = Bike()
bike.start_engine()
