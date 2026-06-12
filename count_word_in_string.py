string="sentence"
for letter in "sentc":
    print(letter,":",string.count(letter))



sentence="sentence"
counts={'s':0,'e':0,'n':0,'t':0,'c':0}
for char in sentence:
    if char in counts:
        counts[char]+=1
print(counts)
