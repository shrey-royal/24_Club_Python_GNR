"""
try:
    # code that may occur exception
except:
    # code that handles the exception
else:
    # code that executes when no exception occurred
"""

def calculate_bmi(height, weight):
    """calculate body mass index (bmi)"""
    return weight / height**2

def evaluate_bmi(bmi):
    """evaluate the bmi"""
    if 18.5 < bmi <= 24.9:
        return 'healthy'
    elif bmi >= 25:
        return 'overweight'

    return 'underweight'

try:
    h = float(input('Enter your height (meters):'))
    w = float(input('Enter your weight (kilograms):'))
except ValueError as e:
    print('Error! please enter a valid input.')
else:
    b = round(calculate_bmi(h, w), 1)
    evaluation = evaluate_bmi(b)

    print(f'Your body mass index is {b}')
    print(f'This is considered {evaluation}')
finally:    # code here gets executed regardless of occurring of exception
    print("YAY!")