class AreaCalculator:
    def area(self, radius=None, length=None, width=None):
        if radius is not None:
            return 3.14 * radius * radius
        elif length is not None and width is not None:
            return length * width
        else:
            raise ValueError("Invalid parameters!")
        
def main():
    calc = AreaCalculator()
    print(calc.area(radius=5))
    print(calc.area(length=4, width=6))

if __name__ == "__main__":
    main()