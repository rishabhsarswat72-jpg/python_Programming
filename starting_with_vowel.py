fruits=["apple", "banana", "cherry", "avocado", "blueberry"]
new_list=[]
for w in fruits:
    vowels="aeiou"
    if w[0] in vowels:
        new_list.append(w)
print(new_list)