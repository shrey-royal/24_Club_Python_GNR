# String Declaration

# var = "String is declared this way"
# print(var, type(var))
# -----------------------------------------------------------
# f_ormatted string (fstring)

# name = input("Enter your name: ")
# greet = f"Hello {name},\nWelcome, to our app"
# greet = f"Hello {input("Enter your name: ")},\nWelcome, to our app"
#
# print(greet)
# -----------------------------------------------------------
# Accessing string element

# s = 'python'
# print(s[-4])
# print(len(s))

# 0 1 2 3 4 5   <- +ve indexing
# p y t h o n

# -6 -5 -4 -3 -2 -1   <- -ve indexing
#  p  y  t  h  o  n
# -----------------------------------------------------------

# Slicing - a TECHNIQUE that helps in extraction of specific words/parts from string.
# syntax: Sequence[start(inclusive):end(exclusive):step-1]

# Positive Slicing
# s = "Artificial_Intelligence"

# print(s[:10])
# print(s[4:10])
# print(s[:4])

# print(f"{s[:4]} from {s[11:16]s}")
# -----------------------------------------------------------
# Step - skip characters

# word = "0_1_2_3_4_5_6_7_8_9"

# print(word[::2])
# print(word[4::4])
# print(word[2::4])
# -----------------------------------------------------------
# Negative Slicing (reverse reading of any iterable data)

# s = "Royal Technosoft Pvt. Ltd."
# print(s[-1:])   # .
# print(s[:-1])   # everything else except the last char

s = "Hello, World!"
# print(len(s))
# print(s[len(s)-3:])
# print(s[-3:])
# print(s[-10:-3])
# print(s[::-1])    # when you put step -1, the string will be reversed
# print(s[-10:-13:-1])
# print(s[-4:-1:1])
# print(s[-1:-4:-1])
# print(s[:0:-1])
# print(s[1:-5:-1])
# print(s[-5:1:-1])

"""
# smol praktis
my_string = "The quick brown fox jumps over the lazy dog"
> reverse a substring from index -10 to -30 with a step of -1
> Extract "dog lazy the over" form the reversed string
> Extract every second character in reverse from the original string
"""