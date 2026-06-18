string = "never odd or even"
clean_text = ""
for char in string:
    if char.isalnum():
        clean_text += char.lower()

longest_palindrome = ""

for i in range(len(clean_text)):
    
    left, right = i,i
    while left >= 0 and right < len(clean_text) and clean_text[left] == clean_text[right]:
        currentLength = right - left + 1
        if currentLength > len(longest_palindrome):
            longest_palindrome = clean_text[left:right+1]
        left -= 1
        right +=1
    left = i
    right=i+1
    while left >= 0 and right < len(clean_text) and clean_text[left] == clean_text[right]:
        currentLength = right - left + 1
        if currentLength > len(longest_palindrome):
            longest_palindrome = clean_text[left:right+1]
        left -= 1
        right += 1

print(longest_palindrome)


    