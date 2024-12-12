def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for item, quantity in inventory.items():
        print(f" - {item} : {quantity} units")

def add_ingredients(inventory):
    ingredient = input("Enter the ingredients to add: ").capitalize()
    try:
        quantity = int(input(f"Enter the quantity for {ingredient}: "))
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        inventory[ingredient] = inventory.get(ingredient, 0) + quantity
        print(f"Added {quantity} units of {ingredient}.")

    except ValueError as e:
        print(f"Error: {e}")

def use_ingredients():
    pass

def low_stock_alert():
    pass


def main():
    inventory = {"Tomato": 10, "Cheese": 5, "Bread": 7}
    threshold = 2

    while True:
        print("\nMenu:")
        print("1. Display Inventory")
        print("2. Add Ingredients")
        print("3. Use Ingredients")
        print("4. Low Stock Alert")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_inventory(inventory)
        elif choice == "2":
            add_ingredients(inventory)
        elif choice == "3":
            use_ingredients(inventory)
        elif choice == "4":
            low_stock_alert(inventory, threshold)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()