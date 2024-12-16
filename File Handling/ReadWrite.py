# file = open('somefile.txt', 'w')
# try:
#     file.write('this is some data udpated')
# except Exception as e:
#     print(e)
# finally:
#     file.close()

"""
file operation modes:
1. 'r' -> open text file for reading text
2. 'w' -> open text file for writing text
3. 'a' -> open text file for appending text
3. '+' -> open text file for updating (both reading & writing)
"""
# ------------------------------------------------------------------
# reading data into file
# ------------------------------------------------------------------

# with open('somefile.txt', 'a') as file:
#     file.write("\nthis is another line of text data")

# with open('somefile.txt', 'r') as file:
#     lines = file.readlines()

# print(lines)
# ------------------------------------------------------------------

# with open('somefile.txt', 'r') as f:
#     contents = f.read()
#     print(contents)

# ------------------------------------------------------------------

# with open('somefile.txt', 'r') as f:
#     [print(line.strip()) for line in f.readlines()]

# ------------------------------------------------------------------

# with open('somefile.txt') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line.strip())

# ------------------------------------------------------------------

with open('anime_dialogues.txt', encoding='utf-8') as f:
    for line in f:
        print(line.strip())