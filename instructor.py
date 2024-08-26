from person import Person
class Instructor(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def __str__(self):
        return f"{super().__str__()}, ID Number: {self.id_number}, Department: {self.department}"