class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def speak(self):
        print(f"{self.name} says {self.sound}!")

class Dog(Animal):
    def fetch(self):
        print(f"{self.name} fetches the ball!")

my_dog = Dog("Rex", "Woof")
my_dog.speak()
my_dog.fetch()