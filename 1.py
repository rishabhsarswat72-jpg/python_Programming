# fruits=["apple", "banana", "cherry", "avocado", "blueberry"]
# new_list=[]
# for w in fruits:
#     if w[0]=='a' or w[0]=='b':
#         new_list.append(w)
# print(new_list)

#remove duplicate in a list and print list without duplicate 
list=[1,2,2,3,4,4]
new_list=[]
for num in list:
    if num not in new_list:
        new_list.append(num)
print(new_list)



str1="listen"
str2="silent"
str2_list=list(str2)
result="yes"

for char in str1:
    found_match=False
    for j in range(len(str2_list)):
        if char==str2_list[j]:
            str2_list[j]=None
            found_match=True
            break
    if not found_match:
        result="no"
        break
print(result)
        
    
        
    
    
        
    
