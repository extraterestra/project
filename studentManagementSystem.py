from person import Person
from student import Student
from instructor import Instructor
from course import Course
from enrollment import Enrollment

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.instructors = {}
        self.courses = {}
        self.enrollments = []

    # Student management methods
    def add_student(self, student):
        if student.id_number in self.students:
            print(f"Student with ID Number {student.id_number} already exists.")
        else:
            self.students[student.id_number] = student

    def remove_student(self, id_number):
        if id_number in self.students:
            del self.students[id_number]
            # Remove all enrollments for this student
            self.enrollments = [enrollment for enrollment in self.enrollments if enrollment.student.id_number != id_number]
        else:
            print(f"Student with ID {id_number} not found.")

    def update_student(self, id_number, name=None, major=None):
        if id_number in self.students:
            student = self.students[id_number]
            if name:
                student.name = name
            if major:
                student.major = major
        else:
            print(f"Student with ID {id_number} not found.")

    # Instructor management methods
    def add_instructor(self, instructor):
        if instructor.id_number in self.instructors:
            print(f"Instructor with ID Number {instructor.id_number} already exists.")
        else:
            self.instructors[instructor.id_number] = instructor

    def remove_instructor(self, id_number):
        if id_number in self.instructors:
            del self.instructors[id_number]
        else:
            print(f"Instructor with ID Number {id_number} not found.")

    def update_instructor(self, id_number, name=None, department=None):
        if id_number in self.instructors:
            instructor = self.instructors[id_number]
            if name:
                instructor.name = name
            if age:
                instructor.age = age
            if department:
                instructor.department = department
        else:
            print(f"Instructor with ID {id_number} not found.")

    # Course management methods
    def add_course(self, course):
        if course.course_id in self.courses:
            print(f"Course with ID {course.course_id} already exists.")
        else:
            self.courses[course.course_id] = course

    def remove_course(self, course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            # Remove all enrollments for this course
            self.enrollments = [enrollment for enrollment in self.enrollments if enrollment.course.course_id != course_id]
            del self.courses[course_id]
        else:
            print(f"Course with ID {course_id} not found.")

    def update_course(self, course_id, course_name=None):
        if course_id in self.courses:
            course = self.courses[course_id]
            if course_name:
                course.course_name = course_name
        else:
            print(f"Course with ID {course_id} not found.")

    # Enrollment management methods
    def enroll_student(self, id_number, course_id):
        if id_number in self.students and course_id in self.courses:
            student = self.students[id_number]
            course = self.courses[course_id]
            course.add_student(student)
            enrollment = Enrollment(student=student, course=course)
            self.enrollments.append(enrollment)
        else:
            print(f"Student ID Number {id_number} or Course ID {course_id} not found.")

    def assign_grade(self, id_number, course_id, grade):
        for enrollment in self.enrollments:
            if enrollment.student.id_number == id_number and enrollment.course.course_id == course_id:
                enrollment.assign_grade(grade)
                return
        print(f"Enrollment not found for Student ID Number{id_number} in Course ID {course_id}.")

    # Retrieval methods
    def get_students_in_course(self, course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            return course.enrolled_students
        else:
            print(f"Course with ID {course_id} not found.")
            return []

    def get_courses_for_student(self, id_number):
        if id_number in self.students:
            student_courses = [enrollment.course for enrollment in self.enrollments if enrollment.student.id_number == id_number]
            return student_courses
        else:
            print(f"Student with ID Number {id_number} not found.")
            return []
