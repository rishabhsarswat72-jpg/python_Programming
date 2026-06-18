a=[1, 3, 5, 7, 3, 9]
b=[3, 5, 5, 8, 9]
new_list=[]
c=[]
for i in a:
    if i in b:
        new_list.append(i)
for w in new_list:
    if w not in c:
        c.append(w)
print(c)
    
        