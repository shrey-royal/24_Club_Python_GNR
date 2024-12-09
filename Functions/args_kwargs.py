"""
# *args -> tuple

def add(*args):
    print(args, type(args), sep='\t')
    return sum(args)

print(add(1, 2, 3, 4, 5, 4, 3, 2, 1))
print(add(1, 2, *[3, 4, 5], 4, 3, 2, 1))
"""
################################################################
# **kwargs -> keyword arguments

def connect(**connection_info):
    print(type(connection_info))
    print(connection_info)

connect(server='localhost', port=8080, user='admin', password='root')

config = {'server': 'localhost', 'port': 8080, 'user': 'admin', 'password': 'root'}
# connect(**config)
connect(connection_info=[1, 2, 3])