class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # Getter/Setter Methods
    # they are public methods which helps user get or set the data of private attributes

    def set_name(self, name: str) -> None:
        self.__name = name if not None else ""

    def get_name(self) -> str:
        return self.__name
    
    def set_age(self, age: int) -> None:
        self.__age = age if not None else 0

    def get_age(self) -> int:
        return self.__age
    
    def __str__(self):  # this method will represent the object
        return f"Myself {self.__name}, I'm {self.__age} years old."
    
def main():
    soniben = Person("Soniben", 89)
    print(soniben)

    soniben.set_name("Vishwa")
    print(soniben.get_name())
    print(soniben.get_age())

if __name__ =="__main__":
    main()

"""
The Getter Setter method works just fine but it has a backward compatibility issue.

to solve this we will use property class

"""