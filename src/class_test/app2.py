class Animal:
    def __init__(self) -> None:
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):    
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


# type m.    and see the magic
m = Mammal()

print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))

# type o.    and see the magic
o = object()

print(issubclass(Mammal, Animal))
print(issubclass(Animal, object))
