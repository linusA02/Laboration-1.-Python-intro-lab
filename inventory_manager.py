import random

# Sample categories
categories = ["Electronics", "Clothing", "Food", "Books", "Home"]

# Initialize inventory with 10 sample products
inventory = [
    {"id": 1, "name": "Laptop", "price": 999.99, "quantity": 10, "category": "Electronics"},
    {"id": 2, "name": "T-shirt", "price": 19.99, "quantity": 50, "category": "Clothing"},
    {"id": 3, "name": "Apple", "price": 0.99, "quantity": 100, "category": "Food"},
    {"id": 4, "name": "Python Book", "price": 29.99, "quantity": 3, "category": "Books"},
    {"id": 5, "name": "Coffee Mug", "price": 12.99, "quantity": 20, "category": "Home"},
    {"id": 6, "name": "Headphones", "price": 79.99, "quantity": 4, "category": "Electronics"},
    {"id": 7, "name": "Jeans", "price": 49.99, "quantity": 15, "category": "Clothing"},
    {"id": 8, "name": "Bread", "price": 2.99, "quantity": 30, "category": "Food"},
    {"id": 9, "name": "Notebook", "price": 5.99, "quantity": 2, "category": "Books"},
    {"id": 10, "name": "Lamp", "price": 39.99, "quantity": 8, "category": "Home"},
]


def display_products():
    print("\n--- All Products ---")

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Quantity: {product['quantity']} | "
            f"Category: {product['category']}"
        )


def add_product():
    print("\n--- Add New Product ---")

    try:
        product_id = int(input("Enter product ID: "))

        # Check if ID already exists
        for product in inventory:
            if product["id"] == product_id:
                print("A product with that ID already exists.")
                return

        name = input("Enter product name: ")

        price = float(input("Enter product price: "))

        quantity = int(input("Enter product quantity: "))

        print("Categories:", ", ".join(categories))
        category = input("Enter product category: ")

        if category not in categories:
            print("Invalid category.")
            return

        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative.")
            return

        new_product = {
            "id": product_id,
            "name": name,
            "price": price,
            "quantity": quantity,
            "category": category,
        }

        inventory.append(new_product)

        print("Product added successfully.")

    except ValueError:
        print("Invalid input. Please enter the correct type of value.")


def update_product():
    print("\n--- Update Product ---")

    try:
        product_id = int(input("Enter the ID of the product to update: "))

        for product in inventory:
            if product["id"] == product_id:

                print("Leave the input empty to keep the current value.")

                name = input(f"Name [{product['name']}]: ")
                price = input(f"Price [{product['price']}]: ")
                quantity = input(f"Quantity [{product['quantity']}]: ")
                category = input(f"Category [{product['category']}]: ")

                if name:
                    product["name"] = name

                if price:
                    product["price"] = float(price)

                if quantity:
                    product["quantity"] = int(quantity)

                if category:
                    if category in categories:
                        product["category"] = category
                    else:
                        print("Invalid category. Category was not changed.")

                print("Product updated successfully.")
                return

        print("Product not found.")

    except ValueError:
        print("Invalid input.")


def remove_product():
    print("\n--- Remove Product ---")

    try:
        product_id = int(input("Enter the ID of the product to remove: "))

        for product in inventory:
            if product["id"] == product_id:
                inventory.remove(product)
                print("Product removed successfully.")
                return

        print("Product not found.")

    except ValueError:
        print("Please enter a valid ID.")


def search_product():
    print("\n--- Search Product ---")

    search_name = input("Enter product name to search for: ").lower()

    found = False

    for product in inventory:
        if search_name in product["name"].lower():
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Price: ${product['price']:.2f} | "
                f"Quantity: {product['quantity']} | "
                f"Category: {product['category']}"
            )
            found = True

    if not found:
        print("No products found.")


def calculate_total_value():
    total = 0

    for product in inventory:
        total += product["price"] * product["quantity"]

    print(f"\nTotal inventory value: ${total:.2f}")


def find_most_expensive():
    if not inventory:
        print("Inventory is empty.")
        return

    most_expensive = inventory[0]

    for product in inventory:
        if product["price"] > most_expensive["price"]:
            most_expensive = product

    print("\n--- Most Expensive Product ---")
    print(f"Name: {most_expensive['name']}")
    print(f"Price: ${most_expensive['price']:.2f}")
    print(f"Quantity: {most_expensive['quantity']}")
    print(f"Category: {most_expensive['category']}")


def find_low_stock():
    print("\n--- Low Stock Products ---")

    found = False

    for product in inventory:
        if product["quantity"] < 5:
            print(
                f"{product['name']} - "
                f"Quantity: {product['quantity']}"
            )
            found = True

    if not found:
        print("No products have low stock.")


def generate_category_report():
    print("\n--- Products by Category ---")

    for category in categories:
        print(f"\n{category}:")

        found = False

        for product in inventory:
            if product["category"] == category:
                print(
                    f"  {product['name']} - "
                    f"${product['price']:.2f} - "
                    f"Quantity: {product['quantity']}"
                )
                found = True

        if not found:
            print("  No products.")


def update_quantities():
    print("\n--- Simulate Sale ---")

    try:
        product_id = int(input("Enter product ID: "))
        amount = int(input("Enter quantity sold: "))

        if amount <= 0:
            print("Quantity must be greater than 0.")
            return

        for product in inventory:
            if product["id"] == product_id:

                if amount > product["quantity"]:
                    print("Not enough stock available.")
                    return

                product["quantity"] -= amount

                print(
                    f"Sale completed. "
                    f"{product['name']} now has "
                    f"{product['quantity']} in stock."
                )
                return

        print("Product not found.")

    except ValueError:
        print("Please enter valid numbers.")


# Main menu logic
while True:
    try:
        choice = int(
            input("""
    1. Display all products
    2. Add a new product
    3. Update a product's information
    4. Remove a product
    5. Search for a product by name
    6. Calculate total inventory value
    7. Find the most expensive product
    8. Find products with low stock
    9. Generate a report of products by category
    10. Update quantities (simulate a sale)
    11. Exit program
    Enter your choice: """)
        )

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 11.")
        continue

    if choice not in range(1, 12):
        print("Invalid choice. Please enter a number between 1 and 11.")
        continue

    if choice == 1:
        display_products()

    elif choice == 2:
        add_product()

    elif choice == 3:
        update_product()

    elif choice == 4:
        remove_product()

    elif choice == 5:
        search_product()

    elif choice == 6:
        calculate_total_value()

    elif choice == 7:
        find_most_expensive()

    elif choice == 8:
        find_low_stock()

    elif choice == 9:
        generate_category_report()

    elif choice == 10:
        update_quantities()

    elif choice == 11:
        print("Exiting program. Goodbye!")
        break