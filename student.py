from person import Person
class Student(Person):
    def __init__(self, name, id_number, major):
        super().__init__(name, id_number)
        self.major = major

    def __str__(self):
        return f"{super().__str__()}, ID Number: {self.id_number}, Major: {self.major}"