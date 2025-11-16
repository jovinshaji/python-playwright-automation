class Bird:
    def fly(self):
        print("Some birds can fly")

class Parrot(Bird):
    def fly(self):
        print("Parrot flies high 🦜")

class Penguin(Bird):
    def fly(self):
        print("Penguin can't fly 🐧")

for bird in [Parrot(), Penguin()]:
    bird.fly()  # Different behavior for each
