def find_best_price(items):
    best_item = None
    best_price = float('inf')  # Initialize with a high price

    for item in items:
        price = item['price']
        if price < best_price:
            best_item = item
            best_price = price

    return best_item

# Example list of items with prices
items = [
    {'name': 'Item 1', 'price': 10},
    {'name': 'Item 2', 'price': 5},
    {'name': 'Item 3', 'price': 8},
    {'name': 'Item 4', 'price': 12}
]

best_item = find_best_price(items)

print(f"The item with the best price is '{best_item['name']}' with a price of {best_item['price']}.")
