# frozen set - immutable and constants
# when a frozen set is declared then it can't be changed

# set1 = frozenset({1, 23, 56, 89, 34, 234})
# print(set1, type(set1), sep='\n')

# transactions = [
#     {"apple", "banana", "milk"},
#     {"apple", "milk"},
#     {"banana", "milk"},
#     {"apple", "banana", "milk"}
# ]
# unique_combinations = set(frozenset(i) for i in transactions)
# print(unique_combinations)

fs = frozenset([1, 2, 3, 4, 5])

fs_union = fs.union([4, 5, 6, 7])
fs_intersection = fs.intersection([2, 3, 4, 5])

print(fs_union, fs_intersection)

"""
# Recap on Data Types
--> List - ordered, mutable & allow duplicates
--> Tuple - ordered, immutable & allow duplicates
--> Set - unordered, mutable & unique
    FrozenSet - unordered, mutable, constant, unique
--> Dictionary - ordered, mutable & unique(keys) , duplicate values are allowed
"""