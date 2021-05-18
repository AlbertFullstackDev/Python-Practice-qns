class Animal:

    def __init__(self):
        self.movement = "locomotion"

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


cat = Mammal()
cat.eat()
print(cat.movement)
