
sentence="sentence"
list=[]
counts={'s':0,'e':0,'n':0,'t':0,'c':0}
for char in sentence:
    if char in counts:
        counts[char]+=1
print(counts)
if counts[char]>1:
    
    print(sentence)
    



paragraph = "My name is akshat my name is short my name rishabh"

words = paragraph.lower().split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

max_count = 0
result=""
for word in word_counts:
    if word_counts[word] > max_count:
        max_count = word_counts[word]
    if word_counts[word] == max_count:
        if result == "" or word < result:
            result = word


print(result)
