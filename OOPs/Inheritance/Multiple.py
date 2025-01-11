class Teacher:
    def __init__(self, name):
        self._name = name

    def teach(self):
        return f"{self._name} is teaching."
    
class Researcher:
    def __init__(self, field):
        self.field = field

    def research(self):
        return f"Researching in the field of {self.field}."
    
class Professor(Teacher, Researcher):
    def __init__(self, name, field):
        Teacher.__init__(self, name)
        Researcher.__init__(self, field)

    def work(self):
        return f"{self.teach()} {self.research()}"
    
def main():
    prof = Professor("Dr. Smit", "AI")
    print(prof.work())

if __name__ == "__main__":
    main()