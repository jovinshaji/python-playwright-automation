class Person:
    def __init__(self, name, age):
        self.name = name       # public attribute
        self.__age = age       # private attribute (using __)

    def get_age(self):         # getter method
        return self.__age

    def set_age(self, age):    # setter method
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

person = Person("Alice", 25)
print(person.name)        # ✅ Accessible
print(person.get_age())   # ✅ Access through getter
person.set_age(30)
print(person.get_age())   # ✅ Updated
# print(person.__age)     # ❌ Error: private variable  