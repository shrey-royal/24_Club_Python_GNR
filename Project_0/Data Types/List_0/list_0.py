"""
List -> Mutable Sequence

syntax:
    list() -> represented by []

Changeable? True
Duplicates Allowed? True
"""

# declaration of list
# myList = []
# myList = list()   # using constructor

# initializing Lists
fruits = ["Mango", "Apple", "Grapes", "Banana", "Orange", "Kiwi", "Dragon Fruit", "Guava", "Watermelon", "Musk Melon", "Mud Apple", "Rose Berry", "Lychee", "Blue Berry", "Black Grapes", "Peach", "Custard Apple", "Papaya", "Pineapple", "Strawberry", "Pomegranate", "Raspberry", "Avocado"]

# print(fruits[2::3])
# print(fruits[::-1])

for fruit in fruits:
    print(fruit)

"""
Q. Convert this list into one sentence and do the following:
    1) print the whole sentence
    2) count how many words are present in the sentence
    3) count how many words starts with the letter n (n will be entered by user)
    4) check how many words are greater than k length (k will be entered by user)
    5) count how many fruits have apple in their names
    6) print all the fruits and count of how many vowels are present in that fruit

"""