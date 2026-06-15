sentence = input("Enter a sentence: ")
words = sentence.split()
capitalized_words = []

for word in words:
    new_word = word[0].upper() + word[1:]
    capitalized_words.append(new_word)
result = " ".join(capitalized_words)
print("Result:", result)
