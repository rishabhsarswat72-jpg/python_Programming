fruits=["apple", "banana", "cherry", "avocado", "blueberry"]
vowels="aeiou"
new_list=[]
for w in fruits:
    no_vowels=""
    for ch in w:
        if ch   not in vowels:
            no_vowels += ch  
    new_list.append(no_vowels) 
print(new_list)        
     