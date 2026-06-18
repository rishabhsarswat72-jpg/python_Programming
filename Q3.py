students = [
    {"name": "rishabh", "age": 20, "grades": [85, 95]},   
    {"name": "ashok", "age": 22, "grades": [90, 100]},   
    {"name": "nikhil", "age": 19, "grades": [95, 95]},
    {"name": "ronak", "age": 21, "grades":[87,89]}     
]


best_student = students[0]
max_average = sum(best_student["grades"]) / len(best_student["grades"])
min_age = best_student["age"]

for student in students[1:]:
    grades = student["grades"]
    current_average = sum(grades) / len(grades)
    current_age = student["age"]
    
    if current_average > max_average:
        max_average = current_average
        min_age = current_age
        best_student = student
    
    elif current_average == max_average:
        if current_age < min_age:
            min_age = current_age
            best_student = student

print("Highest Average Student Details:")
print(best_student)
