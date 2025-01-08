class LivingBeing:
    def __init__(self):
        self.__alive = True

    def is_alive(self):
        return self.__alive
    
    def setAliveStatus(self, aliveStatus):
        self.__alive = aliveStatus
    
class Animal(LivingBeing):
    def __init__(self, species):
        super().__init__()
        self.species = species

class Dog(Animal):
    def __init__(self, name):
        super().__init__("Dog")
        self.name = name

    def display(self):
        return f"{self.name} is a {self.species}. Alive: {self.is_alive()}"

def main():
    dog = Dog("Lucky")
    print(dog.display())
    dog.setAliveStatus(False)
    print(dog.display())

if __name__ == "__main__":
    main()