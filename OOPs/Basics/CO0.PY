class Student:
    rno: int
    name: str
    dhoran: int

    def scanStudent(self, rno: int, name: str, dhoran: int):
        self.rno = rno
        self.name = name
        self.dhoran = dhoran

    def getStdudent(self):
        return f"Roll No.: {self.rno}\nName: {self.name}\nDhoran: {self.dhoran}"

obj1 = Student()    # object

obj1.scanStudent(101, "Brijesh", 3)
print(obj1.getStdudent())


"""
Class and Object Task:

class Ice-Cream with attributes (name, flavor, price) and methods to scan and print the ice-cream

"""