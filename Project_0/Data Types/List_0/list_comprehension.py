"""
List Comprehension: [expression for item in iterable if condition]

for else -> [expression_1 if condition else expression_2 for item in iterable]

"""

# l = [i for i in range(1, 11)]
# l = [i**2 for i in range(1, 11) if i%2 == 0]
l = [i**2 if i%2 == 0 else i for i in range(1, 11)]
print(l)

"""
Tasks:

1. Square of Even Numbers

   Write a Python program to generate a list of squares of even numbers from an existing list of integers using list comprehension. Ignore the odd numbers in the original list.

   Example:
   Input: [1, 2, 3, 4, 5, 6]
   Output: [4, 16, 36]

2. Flatten a Nested List

   Given a list of lists, flatten the nested list into a single list containing all the elements using list comprehension.

   Example:
   Input: [[1, 2], [3, 4], [5, 6]]
   Output: [1, 2, 3, 4, 5, 6]

3. Generate Multiplication Table

   Create a list of lists that represents a multiplication table for numbers 1 through 10 using list comprehension.

   Example:
   Output: [[1, 2, 3, ..., 10], [2, 4, 6, ..., 20], ..., [10, 20, 30, ..., 100]]

4. Filter Words with Specific Length

   Given a list of words, use list comprehension to filter and generate a list of words that have a length greater than 3.

   Example:
   Input: ['apple', 'cat', 'dog', 'banana', 'sky']
   Output: ['apple', 'banana']

5. Convert Fahrenheit to Celsius

   Given a list of temperatures in Fahrenheit, convert them to Celsius using list comprehension. Use the formula:  
   (Celsius = (Fahrenheit - 32) * 5/9)

   Example:
   Input: [32, 50, 77, 104]
   Output: [0.0, 10.0, 25.0, 40.0]

"""