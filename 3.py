class Employee:
    def __init__(self, salary):
        self.salary = salary
        
    def get_bonus(self):
        return self.salary * 0.10

class Manager(Employee):
    def get_bonus(self):
        return self.salary * 0.25

class Intern(Employee):
    def get_bonus(self):
        return 500

emp = Employee(4000)
mgr = Manager(8000)
itn = Intern(2000)

print(emp.get_bonus())
print(mgr.get_bonus())
print(itn.get_bonus())