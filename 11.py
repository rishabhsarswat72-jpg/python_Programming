class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def __str__(self):
        return f"Student: Name={self.name}, Age={self.age}, ID={self.student_id}"

student = Student("Bob", 20, "S12345")
print(student)