print("".center(50, '-'), "Welcome to the Hotel".center(50), "".center(50, '-'), sep='\n')

total: float = 0

while True:
    print("\n--- Main menu ---")
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")
    print("4. Desserts")
    print("5. Beverages")
    print("0. Print Bill")

    choice = int(input("Please choose a category: "))

    match choice:
        case 1:
            print("\n--- Breakfast menu ---")
            print("1. Pancakes - Rs.30")
            print("2. French Toast - Rs.50")
            print("3. Coffee - Rs.10")
            print("0. Go Back to Main menu")
            choice = int(input("Please select any option: "))
            match choice:
                case 1:
                    qty = int(input("How much qty of pancakes you want? -> "))
                    total += qty * 30
                case 2:
                    qty = int(input("How much qty of french toast you want? -> "))
                    total += qty * 50
                case 3:
                    qty = int(input("How much qty of coffee you want? -> "))
                    total += qty * 10
                case 0:
                    print("Going back to main menu...")
                    continue
                case _:
                    print("Sorry! this item is not available for now...")
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 0:
            print(f"Your Total Bill is Rs.{total}")
            print("Thank you for ordering!")
            break
        case _:
            print("Sorry! Please choose a valid option...")