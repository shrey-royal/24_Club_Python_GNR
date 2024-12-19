"""
CSV: Comma-Seperated Values

line 1
line 2
.
.
.
line n

record 1
record 2
.
.
.
record n

Always the first line will be the header line (if the csv  file has a header line)

"""

import csv

# f = open('country.csv')
# csv_reader = csv.reader(f)

# for line in csv_reader:
#     print(line)
# ------------------------------------------------------------------

# with open('country.csv', 'r') as f:
#     reader = csv.reader(f)
#     for line in reader:
#         print(line)
# ------------------------------------------------------------------

# with open('country.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     for line_no, line in enumerate(csv_reader, 1):
#         if line_no == 1:
#             print('Header:')
#             print(line)
#             print('Data:')
#         else:
#             print(line)
# ------------------------------------------------------------------

# with open('country.csv', 'r') as f:
#     csv_reader = csv.reader(f)
    
#     next(csv_reader)

#     for line in csv_reader:
#         print(line)
# ------------------------------------------------------------------

# total_area = 0
# with open('country.csv', 'r') as f:
#     csv_reader = csv.reader(f)
    
#     next(csv_reader)

#     for line in csv_reader:
#         total_area += float(line[1])

# print(total_area)
# ------------------------------------------------------------------

"""
Tasks:

1) Scan a character from the user and then get me all the names of countries who has that letter in it.
2) find me the names of longest and shortest country name.
3) find me the names of longest and shortest country area with all the details of that country.

"""

"""
csv.reader() function has 2 main limitations.

1) the way of accessing the columns is not so obvious.
2) when the order of columns are changed then we also have to make changes into our python to get the right data.


hence, we use DictReader class
"""