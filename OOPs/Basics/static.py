class MathUtils:

    @staticmethod
    def add_numbers(a, b):
        return a+b
    
    @staticmethod   # decorator
    def subtract_number(a, b):
        return a-b


class Car:
    wheels = 4  # class variable

    def __init__(self, brand, color):
        # instance variable
        self.brand = brand
        self.color = color


    
def main():
    # print(MathUtils.add_numbers(2, 3))
    # print(MathUtils.subtract_number(2, 3))

    # Creating instances
    car1 = Car("Toyota", "Red")
    car2 = Car("Honda", "Blue")

    # Accessing attributes
    print(car1.brand)  # Output: Toyota (Instance attribute)
    print(car2.color)  # Output: Blue (Instance attribute)
    Car.wheels = 20
    print(Car.wheels)  # Output: 4 (Class attribute, accessed using the class)


if __name__ == "__main__":
    main()


# make a student class with attributes like name, standard(0, 12) and make multiple objects of that class and store students data into those objects. now count how many students are stored in the class.

"""
-> 1. Basic Calculator with Static Methods
Create a simple calculator class that uses static methods for basic arithmetic operations such as addition, subtraction, multiplication, and division. The class should not require an instance to perform the calculations.

Problem Statement:
Design a Python class `Calculator` with the following static methods:
- `add(a, b)` - Returns the sum of `a` and `b`.
- `subtract(a, b)` - Returns the difference between `a` and `b`.
- `multiply(a, b)` - Returns the product of `a` and `b`.
- `divide(a, b)` - Returns the quotient of `a` divided by `b` (ensure division by zero is handled).

-> 2. Temperature Conversion Utility
Create a class `TemperatureConverter` that uses static methods to convert temperatures between different units (Celsius, Fahrenheit, Kelvin). The class should be able to convert from one unit to another without the need for instantiation.

Problem Statement:
Design a class `TemperatureConverter` with the following static methods:
- `celsius_to_fahrenheit(celsius)` - Converts Celsius to Fahrenheit.
- `fahrenheit_to_celsius(fahrenheit)` - Converts Fahrenheit to Celsius.
- `celsius_to_kelvin(celsius)` - Converts Celsius to Kelvin.
- `kelvin_to_celsius(kelvin)` - Converts Kelvin to Celsius.

-> 3. String Utilities Class
Create a `StringUtils` class that provides static utility methods for string manipulation tasks such as counting vowels, reversing a string, and checking if a string is a palindrome.

Problem Statement:
Design a class `StringUtils` with the following static methods:
- `count_vowels(string)` - Returns the number of vowels in the given string.
- `reverse_string(string)` - Returns the string reversed.
- `is_palindrome(string)` - Checks if the string is a palindrome (reads the same forward and backward).

"""