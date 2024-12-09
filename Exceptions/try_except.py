"""
# try...except -> statement
There are mainly two kinds of errors: syntax errors and exceptions
"""

# print("Before Exception")
# try:
#     a = int(input("Enter int: "))
#     print(a)
# except ValueError as e:
#     print(f"{e}: This exception is handled")

# print("After Exception")

# example - sales growth
"""
print("Enter the net sales for")

previous = float(input(" - Prior period: "))
current = float(input(" - Current period: "))

change = (current - previous) * 100 / previous

if change > 0:
    result = f'Sales increased {abs(change)}%'
else:
    result = f'Sales decreased {abs(change)}%'

print(result)
"""
###################################################################
# Handling the exception
"""
try:
    print("Enter the net sales for")

    previous = float(input(" - Prior period: "))
    current = float(input(" - Current period: "))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increased {abs(change)}%'
    else:
        result = f'Sales decreased {abs(change)}%'

    print(result)

except:
    print('Error! Please enter a number for net sales.')
"""
###################################################################
# Catching specific exception

try:
    print("Enter the net sales for")

    previous = float(input(" - Prior period: "))
    current = float(input(" - Current period: "))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f'Sales increased {abs(change)}%'
    else:
        result = f'Sales decreased {abs(change)}%'

    print(result)

# except ValueError:
#     print('Error! Please enter a number for net sales.')

# except ZeroDivisionError:
#     print('Error! The prior net sales cannot be zero.')

# except (ValueError, ZeroDivisionError) as e:
#     print(f"Error! -> {e}")
#     print("Error occurred!")

except Exception as e:
    print(e)

# -----------------------------------------------------------------------------------

"""
Tasks:

-> Problem Statement 1: Ingredient Price Comparison
You are developing a tool to compare the price change of an ingredient between two shopping trips. The user will input the price of an ingredient during their last shopping trip and its price during the current trip. The tool will calculate the percentage change in price and display whether the price increased or decreased. 

Modify and execute the provided code to:
1. Accept inputs for the previous and current prices of an ingredient.
2. Calculate and display the percentage change in price.
3. Handle the following errors:
   - ValueError: When the user enters non-numeric input for the prices.
   - ZeroDivisionError: When the user enters `0` for the previous price.

-> Problem Statement 2: Restaurant Meal Calorie Change
You are building a calorie-tracking tool for diners to compare the calorie count of a meal between two visits to a restaurant. The user will input the calorie count of a meal from their last visit and its calorie count from the current visit. The tool will compute the percentage change in calories and display whether the calories increased or decreased.

Using the provided code as a base, modify it to:
1. Accept inputs for the previous and current calorie counts of a meal.
2. Compute the percentage change and display whether the calorie count increased or decreased.
3. Handle exceptions with appropriate error messages:
   - If the user provides non-numeric input, print: `"Error! Please enter numeric values for calorie counts."`
   - If the user enters `0` for the previous calorie count, print: `"Error! Previous calorie count cannot be zero to avoid division by zero."`
   - Catch any other unforeseen errors and print: `"An unexpected error occurred: <error_message>"`.

"""