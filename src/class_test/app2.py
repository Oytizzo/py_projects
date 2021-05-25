# class Employee:
#     def greet(self):
#         print("Employee Greet")


# class Person:
#     def greet(self):
#         print("Person Greet")


# class Manager(Employee, Person):
#     pass

# m = Manager()
# m.greet()


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


# Multiple inheritance should not conflict on same functions
class FlyingFish(Flyer, Swimmer):
    pass
