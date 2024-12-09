# Dictionary - Ordered, Mutable and Unique collection containing key-values pairs, where keys are unique and values may get repeated

# myDict = {
#     "key": "value",
#     1: 22,
#     "key1": 3.44,
# }

# myDict = dict()
# print(myDict, type(myDict))

# user_profile = {
#     "username": "soniben",
#     "email": "bizwithsoni@gmail.com",
#     "age": 29,
#     "location": "New York",
#     "preferences": ["technology", "travel", "sports"],
# }

# print(user_profile)
# print(user_profile["email"])

# inventory = {
#     "apples": 50,
#     "bananas": 120,
#     "oranges": 75,
#     "grapes": 30
# }

# print(inventory)
# inventory["apples"] -= 5
# inventory["oranges"] += 10
# inventory["strawberry"] = 100
# print(inventory)

# document = "the quick brown fox jumps over the lazy dog the dog was not amused"
# word_count = {}
#
# for word in document.split():
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# print(word_count)

# address_book = {
#     "Smith Jhonson": {
#         "phone": "0123456789",
#         "email": "jhonson.smith@gmail.com",
#     },
#     "Mridula Alexander": {
#         "phone": "9876543210",
#         "email": "alexander.mridula@gmail.com",
#     },
#     "Tara Cristine": {
#         "phone": "5678901234",
#         "email": "cristine.tara@gmail.com",
#     },
# }

# print(address_book["Mridula Alexander"]["email"])
# print(address_book["Mridula Alexander"]["contact"]) # KeyError

exam_scores = {
    "kartik": [85, 92, 78],
    "pratik": [89, 94, 88],
    "ramesh": [95, 90, 93]
}

pratik_average = sum(exam_scores['pratik']) / len(exam_scores["pratik"])
print(f"{pratik_average:.2f}")

"""
Q) Swap Keys and Values
original_dict = {"a": 1, "b": 2, "c": 3}
-> {1: "a", 2: "b", 3: "c"}

Q) Merge Two Dictionaries
dict1 = {'x': 10, 'y': 20}
dict2 = {'y': 30, 'z': 40}
-> {'x': 10, 'y': 30, 'z': 40}

Q) Remove Key-Value Pairs with Even Values
numbers = {'a': 4, 'b': 3, 'c': 2, 'd': 5}
-> {'b': 3, 'd': 5}

"""