fruit=["apple", "banana", "cherry", "avocado", "blueberry"]
for w in fruit:
    if len(w)>1:
        modified_w=w[0].upper() +w[1:-1] +w[-1].upper()
    else:
        modified_w=w.upper()
    print(modified_w)