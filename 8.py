class Flyable:
    def fly(self):
        print("Flying high!")

class Swimmable:
    def swim(self):
        print("Swimming smoothly!")

class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack quack!")

duck = Duck()
duck.fly()
duck.swim()
duck.quack()