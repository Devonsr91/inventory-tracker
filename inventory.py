
# Small store inventory
inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "keyboard": {"price": 49.99, "quantity": 8},
    "monitor": {"price": 199.99, "quantity": 5}
}


# Display the inventory table
print("\nSTORE INVENTORY")
print("-" * 55)
print(f"{'Product':<15} {'Price':>10} {'Quantity':>10}")
print("-" * 55)

for product, details in inventory.items():
    print(f"{product:<15} ${details['price']:>9.2f} {details['quantity']:>10}")

print("-" * 55)


# Calculate the total inventory value
total_value = 0

for product, details in inventory.items():
    total_value += details["price"] * details["quantity"]

print(f"\nTotal inventory value: ${total_value:,.2f}")


# Look up a product
product_name = input("\nEnter a product to look up: ").lower()
product = inventory.get(product_name)

if product:
    print(f"Product: {product_name}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Quantity: {product['quantity']}")
else:
    print("Product not found.")


# Update a product quantity
update_name = input("\nEnter a product to update: ").lower()
product = inventory.get(update_name)

if product:
    try:
        new_quantity = int(input("Enter the new quantity: "))
        if new_quantity < 0:
            print("Quantity cannot be negative.")
        else:
            product["quantity"] = new_quantity
            print(f"{update_name} quantity updated to {new_quantity}.")
    except ValueError:
        print("Please enter a whole number.")
else:
    print("Product not found.")


# Track products with low stock using a set
low_stock = set()

for product_name, details in inventory.items():
    if details["quantity"] < 10:
        low_stock.add(product_name)

print("\nLOW STOCK ALERT")

if low_stock:
    print("These products need restocking:")
    for product_name in sorted(low_stock):
        print(f"{product_name}: {inventory[product_name]['quantity']} left")
else:
    print("All products have enough stock.")
