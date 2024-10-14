age = int(input("Enter your age: "))

if 0 < age < 100:
    if age <= 18:
        print("Balak")
    elif 18 <= age < 60:
        print("Adult")
    else:
        print("Senior Citizen")
else:
    print("Invalid age input")