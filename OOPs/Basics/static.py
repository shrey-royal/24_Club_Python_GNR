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
    print(Car.wheels)  # Output: 4 (Class attribute, accessed using the class)


if __name__ == "__main__":
    main()


# make a strudent class with attributes like name, standard(0, 12) and make multiple objects of that class and store students data into those objects. now count how many students are stored in the class.