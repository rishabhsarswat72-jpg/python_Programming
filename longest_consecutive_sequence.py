# #You are given a list of integers. Find the longest consecutive sequence.
# Input : [100, 4, 200, 1, 3, 2]
# Output: 4 (sequence: 1,2,3,4)
# Input : [0, -1, 1, 2]
# Output: 4 (sequence: -1,0,1,2)
# Input : [5]
# Output: 1
# Input : [0, -1, 1, 2]
# Output: 4 (sequence: -1,0,1,2)
# Input : [1, 1, 1, 1]
# Output: 1 (duplicates don't extend sequence)
input=[100, 4, 200, 1, 3, 2]
#input.sort()
n=len(input)
for i in range(n):
    for j in range(i+1,n):#[4,100,200,1,3,2]
        #j=2:4>200 no swapping
        #j=3:4>1 ,1 and 4 swapped[1,100,200,4,3,2]
        #j=4:1>3 no swap
        #j=5:1>2 no swap
        #[1,100,200,4,3,2]
        if input[i]>input[j]:
            input[i],input[j]=input[j],input[i]
new_list=[]
new_list.append(input[0])
for i in input:
    
    if i ==(new_list[-1]+1):
        new_list.append(i)
        
print((new_list))
    
    
