import csv

students_list = []


# Grade Function

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Add Student

def add_student():

    print("\n------ Add Student ------")

    student_id = len(students_list) + 1

    name = input("Enter Name : ")

    age = int(input("Enter Age : "))

    n = int(input("How many subjects? "))

    scores = {}

    total = 0

    for i in range(n):

        subject = input("Enter Subject Name : ")

        marks = float(input("Enter Marks : "))

        scores[subject] = marks

        total = total + marks

    average = total / n

    grade = calculate_grade(average)

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "scores": scores,
        "average": round(average,2),
        "grade": grade
    }

    students_list.append(student)

    print("Student Added Successfully")

# View All Students
def view_all_records():

    if len(students_list) == 0:
        print("No Records Found")
        return

    sorted_students = students_list.copy()

    # Bubble Sort
    for i in range(len(sorted_students)):
        for j in range(len(sorted_students)-1):

            if sorted_students[j]["average"] < sorted_students[j+1]["average"]:

                temp = sorted_students[j]
                sorted_students[j] = sorted_students[j+1]
                sorted_students[j+1] = temp

    print("\n" + "-" * 45)
    print(f"{'ID':<6}{'Name':<15}{'Age':<6}{'Average':<29}{'Grade'}")
    print("-" * 45)

    for s in sorted_students:

        print(f"{s['id']:<6}{s['name']:<15}{s['age']:<6}{s['average']:<10}{s['grade']}")


# Search Student
def search_student():

    if len(students_list) == 0:
        print("No Records")
        return

    name = input("Enter Student Name : ")

    found = False

    for s in students_list:

        if name.lower() in s["name"].lower():

            print("\nID :", s["id"])
            print("Name :", s["name"])
            print("Age :", s["age"])
            print("Scores :", s["scores"])
            print("Average :", s["average"])
            print("Grade :", s["grade"])

            found = True

    if found == False:
        print("Student Not Found")
        
# Update Student
def update_student():

    if len(students_list) == 0:
        print("No Records Found")
        return

    student_id = int(input("Enter Student ID to Update : "))

    found = False

    for s in students_list:

        if s["id"] == student_id:

            print("\nCurrent Data:")
            print(s)

            print("\nEnter New Details:")

            name = input("New Name : ")
            age = int(input("New Age : "))

            n = int(input("How many subjects? "))

            scores = {}
            total = 0

            for i in range(n):

                subject = input("Subject Name : ")
                marks = float(input("Marks : "))

                scores[subject] = marks
                total = total + marks

            average = total / n
            grade = calculate_grade(average)

            s["name"] = name
            s["age"] = age
            s["scores"] = scores
            s["average"] = round(average, 2)
            s["grade"] = grade

            print("Student Updated Successfully")

            found = True
            break

    if found == False:
        print("Student Not Found")

# Delete Student
def delete_student():

    if len(students_list) == 0:
        print("No Records Found")
        return

    student_id = int(input("Enter Student ID to Delete : "))

    found = False

    for s in students_list:

        if s["id"] == student_id:

            students_list.remove(s)

            print("Student Deleted Successfully")

            found = True
            break

    if found == False:
        print("Student Not Found")

# Class Statistics
def show_statistics():

    if len(students_list) == 0:
        print("No Records Found")
        return

    total_students = len(students_list)

    total_avg = 0

    highest = students_list[0]
    lowest = students_list[0]

    grade_count = {"A":0, "B":0, "C":0, "D":0, "F":0}

    for s in students_list:

        total_avg = total_avg + s["average"]

        if s["average"] > highest["average"]:
            highest = s

        if s["average"] < lowest["average"]:
            lowest = s

        grade_count[s["grade"]] = grade_count[s["grade"]] + 1

    print("\n----- CLASS STATISTICS -----")
    print("Total Students :", total_students)
    print("Class Average :", round(total_avg / total_students, 2))

    print("\nHighest Scorer :")
    print(highest["name"], highest["average"])

    print("\nLowest Scorer :")
    print(lowest["name"], lowest["average"])

    print("\nGrade Distribution:")
    for g in grade_count:
        print(g, ":", grade_count[g])
        
# Save to CSV
def save_to_csv():

    if len(students_list) == 0:
        print("No Records to Save")
        return

    file = open("students.csv", "w", newline="")

    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Age", "Scores", "Average", "Grade"])

    for s in students_list:

        score_str = ""

        for subject in s["scores"]:
            score_str = score_str + subject + ":" + str(s["scores"][subject]) + " "

        writer.writerow([
            s["id"],
            s["name"],
            s["age"],
            score_str,
            s["average"],
            s["grade"]
        ])

    file.close()

    print("Data Saved Successfully in students.csv")

# Load from CSV
def load_from_csv():

    global students_list

    try:
        file = open("students.csv", "r")

        reader = csv.reader(file)

        next(reader)  # skip header

        students_list = []

        for row in reader:

            scores = {}

            if row[3] != "":
                parts = row[3].split()

                for p in parts:
                    if ":" in p:
                        sub, mark = p.split(":")
                        scores[sub] = float(mark)

            student = {
                "id": int(row[0]),
                "name": row[1],
                "age": int(row[2]),
                "scores": scores,
                "average": float(row[4]),
                "grade": row[5]
            }

            students_list.append(student)

        file.close()

        print("Data Loaded Successfully")

    except:
        print("File Not Found or Error Reading File")

# Main Menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Class Statistics")
    print("7. Save to CSV")
    print("8. Load from CSV")
    print("9. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_all_records()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        show_statistics()

    elif choice == "7":
        save_to_csv()

    elif choice == "8":
        load_from_csv()

    elif choice == "9":
        print("Thank You!")
        break

    else:
        print("Invalid Choice") 