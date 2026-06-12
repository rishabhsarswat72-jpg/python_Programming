fruits=["apple", "banana", "cherry", "avocado", "blueberry"]
new_list=[]
for w in fruits:
    swapped=w[-1]+w[1:-1] +w[0]
    new_list.append(swapped)
print(new_list)
    