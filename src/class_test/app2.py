class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass

c = Chicken()
# chicken cannot fly
c.fly()
c.eat()
