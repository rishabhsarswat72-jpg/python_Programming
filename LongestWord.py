sentence="hello rishabh"
word=sentence.split()
Longest_word=""
for w in word:
    better_word=w.strip(".,")
    if len(better_word)>len(Longest_word):
        Longest_word=better_word
        
print(Longest_word)