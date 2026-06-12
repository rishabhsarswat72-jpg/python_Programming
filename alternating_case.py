fruits=["apple", "banana", "cherry", "avocado", "blueberry"]
final_list=[]
for w in fruits:
    new_fruits=""
    for i in range(len(w)):
        if i%2==0:
            new_fruits+=w[i].upper()
        else:
            new_fruits+=w[i].lower()
    final_list.append(new_fruits)
print(final_list)
    