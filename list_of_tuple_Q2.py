inventory = [("pen", 5, 100), ("book", 50, 30), ("bag", 200, 10)]

total_value = 0
max_price = 0
most_expensive_product = ""
for product, price, quantity in inventory:
    total_value += price * quantity
    print(total_value)
    if price > max_price:
        max_price = price
        most_expensive_product = product

print(f"Total Inventory Value: {total_value}")
print(f"Most Expensive Product: {most_expensive_product}")