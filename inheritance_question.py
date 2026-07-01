#**Q1.** What does inheritance let you do, and what is the syntax to make `Dog` inherit from `Animal`?
class Animal:
    def __init__(self, name):
        self.name=name
        
    def speak(self):
        return "I am an animal"
class Dog(Animal):
    def __init__(self, name, bark):
        super().__init__(name)
        self.bark=bark
        
    def speak(self):
        return f"{self.name} says {self.bark}"
r=Dog("budddy","woof")
print(r.speak())


#**Q3.** What is method overriding?
#method overriding is a feature in object-oriented programming that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. When a method in a subclass has the same name,return type,and parameters as a method in its superclass,the subclass's method overrides the superclass's method.


#question 4
class Employee:
    def __init__(self, name, salary):
        self.name, self.salary = name, salary
    def get_bonus(self):
        return self.salary * 0.10

class Intern(Employee):
    def get_bonus(self):
        return 500
print(Intern("Carol", 30000).get_bonus())



#**Q7.** Write a `Square` class that reuses `Rectangle.__init__` using `super()`.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def area(self):
        return self.width *self.height

s=Square(5)
print(s.area())

#**Q8.** What is multiple inheritance? Give the syntax.
# Multiple inheritance allows a class to inherit from more than one parent class. The syntax is: class ChildClass(ParentClass1, ParentClass2, ...)

#question 9 * In the diamond pattern below, what does `d.hello()` print and why?
class A:
    def hello(self): print("A")
class B(A):
    def hello(self): print("B")
class C(A):
    def hello(self): print("C")
class D(B, C): pass
d = D()
d.hello()

#d.hello() prints "B" because class D inherits from both B and C, but B is listed first in the inheritance order. Therefore, the method resolution order (MRO) will prioritize the hello method from class B over class C.


#question 10 * What is the method resolution order (MRO) in Python?
# The method resolution order (MRO) in Python is the order in which base classes are searched when executing a method. It determines the sequence in which classes are looked up for methods and attributes. Python uses the C3 linearization algorithm to compute the MRO, ensuring a consistent and predictable order of inheritance, especially in cases of multiple inheritance. You can view the MRO of a class using the `__mro__` attribute or the `mro()` method.

#question 14
class Flyable: pass
class Duck(Flyable): pass
d = Duck()
print(isinstance(d, Duck))
print(isinstance(d, Flyable))
print(isinstance(d, str))


#**Q17.** Override `__str__` so that `print(p)` shows `Point(3, 4)`.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
p=Point(3, 4)
print(p)
#**Q18.** Will this work? Explain.
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks!")

Dog("Rex").bark()



#**Q20.** Write a type-safe function that prints a rectangle's area only if given a `Rectangle` (or subclass), otherwise prints "Unknown shape".
import typing
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_area(self):
        area = self.width * self.height
        print(f"Area: {area}")
        
class Circle:
    def __init__(self, radius):
        self.radius = radius

def print_rectangle_area(shape: any) -> None:
    if isinstance(shape, Rectangle):
        print(f"Rectangle Area: {shape.width * shape.height}")
    else:
        print("Unknown shape")
rect = Rectangle(5, 3)
rect.print_area()
print_rectangle_area(rect)
print_rectangle_area(Circle(4))


#**Q19.** A child overrides `area()`, and the parent's `info()` calls `self.area()`. Which `area()` runs when called on a child instance?give program
class Shape:
    def area(self):
        return 0

    def info(self):
        return f"Area: {self.area()}"
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.info())
c=Circle(20)
print(c.info())
