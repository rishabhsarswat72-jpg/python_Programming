
paragraph = input("Enter text: ")
words = paragraph.lower().split()
most_word = ""
max_count = 0
for current_word in words:
    
    current_count = 0
    for match_word in words:
        if match_word == current_word:
            current_count += 1


    if current_count > max_count:
        max_count = current_count
        most_word = current_word


print("Most frequent word:", most_word)
print("Count:", max_count)

