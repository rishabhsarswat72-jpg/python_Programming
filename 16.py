class Employee:
    def __init__(self, salary):
        self.salary = salary
    def raise_salary(self, pct):
        self.salary += self.salary * (pct / 100)

class Manager(Employee):
    def raise_salary(self, pct):
        super().raise_salary(pct)
        self.salary += 1000

mgr = Manager(5000)
mgr.raise_salary(10)
print(mgr.salary)