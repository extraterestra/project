class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []

    def add_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
        else:
            print(f"{student.name} is already enrolled in {self.course_name}.")

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
        else:
            print(f"{student.name} is not enrolled in {self.course_name}.")        

    def __str__(self):
        student_names = ', '.join(student.name for student in self.enrolled_students)
        return f"Course Name: {self.course_name}, Course ID: {self.course_id}, Enrolled Students: [{student_names}]"

