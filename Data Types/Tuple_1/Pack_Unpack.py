# packing is when you assign multiple values to a single variable.

# var = 1, 2, 3   # this will pack 1, 2, 3 into a tuple named var
# var = (1, 2, 3)
# print(var, type(var))

# Unpacking is a process of assigning each value in tuple to a variable

# data = (1, 2, 3)
# a, b, c = data
# print(a, b, c)

# import random

# numbers = [random.randint(0, 100) for _ in range(10)]
# numbers = 41, 13, 96, 35, 19, 85, 22, 33, 75, 68
# print(numbers)

# n1, _, n2, n3 = 41, 13, 96, 35
# print(n1, n2, n3)

# n1, n2, *n3 = numbers
# n1, *n2, n3 = numbers
# *n1, n2, n3 = numbers
# print(n1, n2, n3)

my_tuple = (1, (2, 3), 4)
a, (b, c), d = my_tuple

print(a, b, c, d)

"""
-> Task 1: Basic Unpacking
Given a tuple "student_info = ("Alice", 21, "Biology")", unpack it into variables "name", "age", and "major", and print each of them.

-> Task 2: Ignoring Values
Given a tuple "colors = ("red", "green", "blue", "yellow")", unpack it so that only the first and last colors are assigned to variables ("first_color" and "last_color") and print these two variables.

-> Task 3: Packing with Arbitrary Values
Create a tuple named "prices" containing several price values: "(19.99, 9.99, 4.99)". Unpack these values into separate variables and calculate the total price by summing them.

-> Task 4: Unpacking with "*"
Given a tuple "numbers = (10, 20, 30, 40, 50, 60)", unpack it so that the first number is assigned to a variable "start", the last number to "end", and the remaining middle values to a list "middle_values". Print all three variables.

-> Task 5: Nested Tuple Unpacking
Suppose you have a tuple "employee_record = ("John Doe", (35, "Engineer"), "San Francisco")". Unpack it into variables "name", "details", and "location". Then unpack "details" further into "age" and "position". Print all variables.

-> Task 6: Swapping Variables Using Tuple Unpacking
Create two variables "x = 5" and "y = 10". Use tuple packing and unpacking to swap their values without using a temporary variable. Print the swapped values.

-> Task 7: Tuple Unpacking in a Loop
Given a list of tuples with pairs of numbers, "pairs = [(1, 2), (3, 4), (5, 6)]", use a "for" loop with unpacking to iterate through each tuple and print the sum of each pair.

-> Task 8: Unpacking in Place
Given a list of numbers "values = [4, 1, 9, -3, 5]", find the minimum and maximum values using "min()" and "max()", and unpack the results into "min_val" and "max_val". Print these values.

-> Task 9: Grouping and Unpacking for Unknown-Length Data
You have a list "data = [100, 200, 300, 400, 500]". Unpack it so that:
- "first" contains the first item.
- "last" contains the last item.
- "middle" contains all items in between as a list.
Print all three variables.

-> Task 10: Creating Multiple Tuples and Unpacking Simultaneously
Create two tuples, "a = (1, 2, 3)" and "b = (4, 5, 6)". Use tuple unpacking to swap their contents and print the new values of "a" and "b".

-> Additional Task: Unpacking in a Nested Structure
Given a list of tuples "nested_data = [(1, 2), (3, 4), (5, 6)]", unpack the list in a way that you create two separate lists: one for the first elements and one for the second elements. Print both lists. 
"""