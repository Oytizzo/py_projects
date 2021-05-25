class Animal:
    def __init__(self) -> None:
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self) -> None:
        # super().__init__()
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


# type m.    and see the magic
m = Mammal()
print(m.age)
print(m.weight)
