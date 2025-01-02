class FoodItem:
    # constructor (default)
    # def __init__(self):
    #     self.name = ""  # Name of the food item (e.g., "Apple", "Pizza")
    #     self.category = ""  # Category (e.g., "Fruit", "Fast Food", "Dessert")
    #     self.price = 0.0  # Price in inr currency
    #     print("Default Constructor called!")

    # constructor (parameterized)
    # def __init__(self, name: str, category: str, price: float):
    #     self.name = name
    #     self.category = category
    #     self.price = price
    #     print("Parameterized Constructor called!")

    def __init__(self, name: str = "", category: str = "", price: float = 0.0):
        self.name = name
        self.category = category
        self.price = price

    def getFoodItem(self) -> str:
        return f"{self.name} is a {self.category} that costs {self.price: .2f} rupees."
    

def main():
    chaas = FoodItem("Chaas", "Beverage", 20)
    lassi = FoodItem("Lassi", "Dessert", 120)

    print(chaas.getFoodItem(), lassi.getFoodItem(), sep='\n')

if __name__ == "__main__":
    main()