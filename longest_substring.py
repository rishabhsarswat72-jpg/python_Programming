string = ""
result = ""
max_substring = ""

for w in string:
    if w in result:
        
        result = result[result.index(w) + 1:]
    
    result += w
    if len(result) > len(max_substring):
        max_substring = result

print(f"'{max_substring}' (length {len(max_substring)})")

        
    