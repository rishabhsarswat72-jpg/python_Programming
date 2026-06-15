list=["hi there","Go","i love python", "Rohit Jain!!! !","ok fine"]
new_list=[]
for w in list:
    word=w.split()
    word_count=len(word)
    new_list.append(word_count)
n=len(list)
for i in range(n):
    for j in range(0,n-i-1):
        if new_list[j]>new_list[j+1]:
            temp_count=new_list[j]
            new_list[j]=new_list[j+1]
            new_list[j+1]=temp_count
            
            temp_sentence=list[j]
            list[j]=list[j+1]
            list[j+1]=temp_sentence
            
print(list)
            
            
    