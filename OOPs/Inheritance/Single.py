class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def display_brand(self):
        return f"Brand: {self.brand}"
    
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_details(self):
        return f"{super().display_brand()}, Model: {self.model}"
    

def main():
    c = Car("Maruti-Suzuki", "Omni-E")
    # print(c.display_brand())
    print(c.display_details())

if __name__ == "__main__":
    main()