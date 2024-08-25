class Enrollment:
    def __init__(self, student, course, grade=None):
        self.student = student
        self.course = course
        self.grade = grade

    def assign_grade(self, grade):
        self.grade = grade


    def __str__(self):
        return f"Student: {self.student.name}, Course: {self.course.course_name}, Grade: {self.grade if self.grade is not None else 'Not graded yet'}"