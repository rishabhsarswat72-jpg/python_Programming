
students = [("Alice", 85),("Alice",90),("Bob", 92), ("Charlie", 85), ("David", 92)]
students.sort()
print(students)
swapped_list = []
for name, marks in students:
    swapped_list.append((marks,name))

swapped_list.sort(reverse=True)
print(swapped_list)
final_list = []
for marks, name in swapped_list:
    final_list.append((name, marks))
print(final_list)
