"""
Functions --> Assistants
=> A Function is a named code block that performs a job and may or may not return a value

syntax:
def function_name(argument/s):
    //body of the function
"""
# import datetime as dt

# def greet() -> str:
#     now = dt.datetime.now()
#     current_hour = now.hour

#     if 5 <= current_hour < 12:
#         greetings = "Good morning!"
#     elif 12 <= current_hour < 17:
#         greetings = "Good afternoon!"
#     elif 17 <= current_hour < 21:
#         greetings = "Good evening!"
#     else:
#         greetings = "Good night!"

#     return greetings

# print(greet())
######################################################################

# Doc Strings (Documentation String)

# def custom_print(message):
#     """This function takes a string as message and print that message"""
#     print(message)

# custom_print("We are learning Python")
######################################################################

# def greet(name: str) -> None:
#     print(f"Hi, {name}")
#
# greet(input("Enter your name: "))
######################################################################

# def addition(a: int, b: int = 0) -> int:            # Default Parameter
#     return a+b
#
#
# def subtraction(a: int, b: int) -> None:
#     print(a-b)


# print(addition(2, 3))
# subtraction(323, 21)

# print(addition(32))
######################################################################

# smol praktis
# Problem Statement: Create a function 'greet_user' that takes two parameters: 'name' (a string) and 'greeting' (a string). The greeting parameter should have a default value of "Hello". The function should print a message in the format: "greeting, name!". If no greeting is provided, it should use the default value.
######################################################################

# named parameters

# def addition(a: int | float = 10, b: int | float = 5) -> int | float:
#     return a + b

# print(addition(23, 3))
# print(addition(3))
# print(addition(b=23))

# def greet(name, greeting):
#     print(f"{greeting}, {name}")

# greet("Dharmik", "Hello")
# greet(greeting="Hii", name="Dharmik")
######################################################################

# Recursive Function

def factorial(num=0):
    # base condition
    if num == 0:
        return 0
    elif num == 1:
        return 1

    # recursion
    return num * factorial(num - 1)

print(factorial(5))

"""
Tasks:
reverse_string(str) -> str
sum_of_digits(num) -> int
is_leap_year(year) -> bool
"""