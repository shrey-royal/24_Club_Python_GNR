# Anonymous Functions
# lambda parameters: expression => syntax

# varaible = lambda parameter: expression => function definition
# variable(parameter)   => function calling

# Normal func
# def square(x):
#     return x**2
#
# ans = square(4)

# lambda func
# ans = lambda x: x**2
# print(ans(7))

# lambda with multiple params
# add = lambda a, b=0: print(f"{a} + {b} = {a+b}")
# add(b=2, a=34)

# lambda with parameterless func
# greet = lambda : "Hello!"
# print(greet())

# print((lambda x: x**3)(4))

# -----------------------------------------------------------------------------------------------------

# import random

# pairs = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(5)]
# print(pairs)

# map(function, iterable) -> used to process data (work with any function)

# Normal func
# def map_func(elem):
#     return elem[0]*elem[1]

# mappedList = list(map(map_func, pairs))
# print(mappedList)

# Lambda func
# mappedList = list(map(lambda elem: elem[0] * elem[1], pairs))
# print(mappedList)
#######################################################

# filter function
# filter(function, iterable) -> used with boolean function

# Normal func
# def filter_func(elem):
#     max_elem = max(elem[0], elem[1])
#     return max_elem > 7

# filteredList = list(filter(filter_func, pairs))
# filteredList = list(filter(lambda elem: max(elem[0], elem[1]) > 7, pairs))
# print(filteredList)
#######################################################

# sorted
# myList = [67, 56, 43, 23, 435, 456, 67, 3, 23, 23, 2]
# sortedList = list(filter(lambda x: x%2 == 0, sorted(myList)))
# sortedList = sorted(myList, key=lambda x: -x)
# sortedList = sorted(pairs, key=lambda x: x[0])
# print(sortedList)

# fruits = [(1, '🍉'), (2, '🍒'), (3, '🍎'), (4, '🍅')]
# sortedFruits = sorted(fruits, key=lambda x: -x[0])
# print(sortedFruits)

# num_list = [23, 345, 234, 56, 23, 45, 567]
# s1 = sorted(num_list, key=lambda x: x)
# s2 = sorted(num_list, key=lambda x: x%10)
# print(s1)
# print(s2)
#######################################################

# reduce(function, sequence, initializer(optional)): apply function on all the elems of sequence
from functools import reduce

# def max(a, b):
#     return a if a>b else b

# myList = [211, 4, 6, 8, 10, 11]
# print(reduce(max, myList))
# pairs = [random.randint(1, 10) for _ in range(5)]
# print(pairs)
# print(reduce(lambda x, y: x*y, pairs))
#######################################################

# myList = [True if random.randint(0, 2) == 1 else False for _ in range(11)]
# myList = [False, False, False, True, False, True, False, True, False, False, True]
# print(myList)

# any (or operator)
# print(any(myList))

# all (and operator)
# print(all([True, True, True, True, 2, 2.3, 's', "22", False]))

multiple_of_6 = list(not (i % 6) for i in range(1, 11))
print(multiple_of_6)
print(any(multiple_of_6))   # or
print(all(multiple_of_6))   # and