# fruits=["apple", "banana", "cherry", "avocado", "blueberry"]
# new_list=[]
# for w in fruits:
#     if w[0]=='a' or w[0]=='b':
#         new_list.append(w)
# print(new_list)



str1="learn"
str2="Python"
str2_list=list(str2)
result="yes"
for i in range (len(str1)):
    char=str1[i]
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
        
    
        
    
    
        
    
