file_name = input("Enter name of the file: ") + '.txt'

with open(file_name, 'w+') as f:
    f.write(input("Enter the data you want to insert into " + file_name + ": "))

    # resetting the cursor back to 0
    f.seek(0)

    print("File Content:\n")
    print(f.read())

f.close()