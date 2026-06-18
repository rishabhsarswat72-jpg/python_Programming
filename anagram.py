#1st method
words=["eat and repeat", "tea", "tan", "ate and repeat", "nat", "bat"]
groups={}
for word in words:
     key="".join(sorted(word))
     if key not in groups:
         groups[key]=[]
        
     groups[key].append(word)
     
result=list(groups.values())
print(result)

#2nd method
input=["eat", "tea", "tan", "ate", "nat", "bat"]
output=[]
for anagram in input:
    group=[]
    for word in input:
        for i in anagram:
            for j in word:
                if i==j:
                    break
            else:
                break
        else:
            group.append(word)
    if group not in output:
        output.append(group)
print(output)
            
                
                
                
            

         
 