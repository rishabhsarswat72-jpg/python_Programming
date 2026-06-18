#4. You are given a dictionary of employees where each key is an employee ID and value is an object with name, department, and salary. Group employees by department and find the highest paid in each department.
employee={
    101:{"name":"rishabh","department":"Cse","salary":60000},
    102:{"name":"nikhil","department":"Cse","salary":70000},
    103:{"name":"ashok","department":"IT","salary":90000},
    104:{"name":"ronak","department":"IT","salary":80000}   
}
highest_salary={}
highest_employee={}
for emp_id,info in employee.items():
    dept=info["department"]
    salary=info["salary"]
    name=info["name"]
    
    if dept not in highest_salary:
        highest_salary[dept]=salary
        highest_employee[dept]=name
    
        
    elif salary>highest_salary[dept]:
        highest_salary[dept]=salary
        highest_employee[dept]=name
    print(highest_salary)
for dept in highest_salary:
    print(f"(salary:{highest_salary[dept]})  {dept}:{highest_employee[dept]}")
