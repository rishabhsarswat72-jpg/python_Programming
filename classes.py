# Q1. Write a class Robot with a class attribute kind = "machine"
#     and a method greet(self) that prints "Beep boop!". Create an
#     instance and call greet().
class Robot:
    kind="machine"
    def greet(self):
        print("beep boop!")
c=Robot()
c.greet()

# Q2. Write a class Book whose __init__ takes title, author, and
#     pages, storing each on self. Add a summary() method printing
#     "<title> by <author>, <pages> pages". Create one book and
#     call summary().
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def summary(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")

my_book = Book("1984", "Rishabh", 328)
my_book.summary()

# Q3. Write a class Rectangle whose __init__ takes width and height
#     with height defaulting to 10. Add an area() method. Create one
#     rectangle using the default and print its area.
class Rectangle:
    def __init__(self,width,height=10):
        self.width=width
        self.height=height
    def Area(self):
        area=self.width*self.height
        print(f"area of ractangle is:{area}")
a=Rectangle(7)
a.Area()

# Q4. Write a class Student that keeps a shared count of how many
#     students have been created. After creating three students,
#     print the total.
class Student:

    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1
student1 = Student("A")
student2 = Student("B")
student3 = Student("C")
student4 = Student("D")
print(f"Total students created: {Student.total_students}")

# Q5. Write a class Temperature with a class attribute
#     unit = "Celsius" and an __init__ taking degrees. Add a
#     describe() method that prints "<degrees> <unit>".
class Temperature:
    unit = "Celsius"

    def __init__(self, degrees):
        self.degrees = degrees

    def describe(self):
        print(f"{self.degrees} {Temperature.unit}")
temp = Temperature(25)
temp.describe()

#question 6
class Car:
        def __init__(self, year):
            self.year = year
 
a = Car(2022)
b = Car(2024)
a.year = 2023
print(a.year, b.year)#2023 2024

#question 7

class Employee:
        company = "TechCorp"
 
e1 = Employee()
e2 = Employee()
Employee.company = "NewTech"
print(e1.company, e2.company)#NewTech NewTech

#question 8
class Employee:
        company = "TechCorp"
 
e1 = Employee()
e2 = Employee()
e1.company = "Freelance"
print(e1.company, e2.company)
print(Employee.company)

#question 9
class Config:
        def __init__(self, host, port):
            self.host = host
            self.port = port
 
cfg = Config("localhost", 8080)
for attr in ["host", "timeout"]:
        if hasattr(cfg, attr):
            print(attr, "=", getattr(cfg, attr))
        else:
            print(attr, "= (not set)")

#question 10
class Team:
        members = []      
 
        def add(self, name):
            self.members.append(name)
 
t1 = Team()
t2 = Team()
t1.add("Alice")
t2.add("Bob")
print(t1.members)
print(t2.members)
#question 11
class Circle:
        def __init__(self, radius):
            self.radius = radius      # bug
 
        def area(self):
            return 3.14159 * self.radius ** 2
c=Circle(5)
print(c.area())
#question 12
class Greeter:
        def hello(self):
            print("Hi!")
 
g = Greeter()
g.hello()
#question 13
class Config:
        def __init__(self, host, port, debug):
            self.host = host    # bug: should be self.host
            self.port = port
            self.debug = debug
 
cfg = Config("localhost", 8080, True)
print(cfg.host)

# Q14. Write a BankAccount class with __init__(self, owner, balance=0).
#      Add deposit(amount) that rejects non-positive amounts, and
#      withdraw(amount) that rejects non-positive amounts and refuses
#      to overdraw (printing "Insufficient funds."). Demonstrate a
#      successful deposit, a successful withdrawal, and a failed
#      overdraw.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount

account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
# Q15. Extend BankAccount with a class variable interest_rate = 0.03
#      and a private-by-convention list self._history. Add
#      apply_interest() that adds interest to the balance and logs it,
#      and a print_statement() that prints every history entry and the
#      final balance. Show that changing BankAccount.interest_rate
#      affects all accounts.
class BankAccount:
    interest_rate = 0.03

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self._history = [f"Initial balance: ${balance:.2f}"]

    def deposit(self, amount):
        if amount <= 0:
            return
        self.balance += amount
        self._history.append(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self._history.append(f"Withdrew: ${amount:.2f}")

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        self._history.append(f"Interest applied: ${interest:.2f} (at {BankAccount.interest_rate * 100:.1f}%)")

    def print_statement(self):
        print(f"\n--- Statement for {self.owner} ---")
        for entry in self._history:
            print(entry)
        print(f"Final Balance: ${self.balance:.2f}")
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 2000)

BankAccount.interest_rate = 0.05

account1.apply_interest()
account2.apply_interest()
account1.print_statement()
account2.print_statement()


        
