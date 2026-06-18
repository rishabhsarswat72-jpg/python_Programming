str="racecar"
reverse_string=""
for w in range(len(str)-1,-1,-1):
    reverse_string+=str[w]
print("reverse string is",reverse_string)
if str==reverse_string:
    print("string is palindrome")
    
    
    
    
    