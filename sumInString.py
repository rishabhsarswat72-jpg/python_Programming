string=input("enter a string with mixed number:")
sum=0
for char in string:
    if char.isdigit():
        sum+=int(char)
print(sum)
