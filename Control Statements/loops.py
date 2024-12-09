"""
Loop: Entry-Controlled Loop

1. for: fixed iteration
syntax:
    for iterator_var in iterable:
        # body

2. while: unfixed iteration
syntax:
    while condition:
        # body

"""

# range(start=0, stop-1, step=1) function

# for i in range(10):
#     print(i, end=", ")
# print("\b\b ")

# user_input = int(input("Enter the end: "))
# for i in range(user_input):
#     print(i, end=', ')

# i = 1
# while i <= 10:
#     print(i, end=', ')
#     i+=1

######################################################################

choice = 1
while choice != 0:
    print("1. Tea\n2. Coffee\n3. Milkshake\n4. Lassi\n0. Exit")
    choice = int(input("Enter your choice: "))
    if 0 < choice <= 4: print("Good!")
    elif choice == 0: continue
    else: print("Invalid choice! Try Again")