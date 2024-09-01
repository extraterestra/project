from person import Person
from student import Student
from instructor import Instructor
from course import Course
from enrollment import Enrollment

class StudentManagementSystem:
    """Class class StudentManagementSystem"""
    def __init__(self):
        self.students = {}
        self.instructors = {}
        self.courses = {}
        self.enrollments = []

    # Student management methods
    def add_student(self, student:object) -> None:
        """
        Function to add students to LMS
        :param student: student object
        """
        if student.id_number in self.students:
            print(f"Student with ID Number {student.id_number} already exists.")
        else:
            self.students[student.id_number] = student

    def remove_student(self, id_number:str) -> None:
        """
        Function to remove students from LMS
        :param id_number: id of person
        """
        if id_number in self.students:
            del self.students[id_number]
            # Remove all enrollments for this student
            self.enrollments = [enrollment for enrollment in self.enrollments if enrollment.student.id_number != id_number]
        else:
            print(f"Student with ID {id_number} not found.")

    def update_student(self, id_number:str, name=None, major=None) -> None:
        """
        Function to update student object in LMS
        :param id_number: id of person
        :param name: name of person
        :param major: major of student
        """
        if id_number in self.students:
            student = self.students[id_number]
            if name:
                student.name = name
            if major:
                student.major = major
        else:
            print(f"Student with ID {id_number} not found.")

    # Instructor management methods
    def add_instructor(self, instructor:object) -> None:
        """
        Function to add instructor to LMS
        :param instructor: instructor object
        """
        if instructor.id_number in self.instructors:
            print(f"Instructor with ID Number {instructor.id_number} already exists.")
        else:
            self.instructors[instructor.id_number] = instructor

    def remove_instructor(self, id_number:str) -> None:
        """
        Function to remove instructor from LMS
        :param instructor: instructor object
        """
        if id_number in self.instructors:
            del self.instructors[id_number]
        else:
            print(f"Instructor with ID Number {id_number} not found.")

    def update_instructor(self, id_number:str, name=None, department=None) -> None:
        """
        Function to update instructor object in LMS
        :param id_number: id of person
        :param name: name of person
        :param department: department of instructor
        """
        if id_number in self.instructors:
            instructor = self.instructors[id_number]
            if name:
                instructor.name = name
            if department:
                instructor.department = department
        else:
            print(f"Instructor with ID {id_number} not found.")

    # Course management methods
    def add_course(self, course:object) -> None:
        """
        Function to add course to LMS
        :param course: course object
        """
        if course.course_id in self.courses:
            print(f"Course with ID {course.course_id} already exists.")
        else:
            self.courses[course.course_id] = course

    def remove_course(self, course_id:str) -> None:
        """
        Function to remove course from LMS
        :param course_id: course_id string
        """
        if course_id in self.courses:
            course = self.courses[course_id]
            # Remove all enrollments for this course
            self.enrollments = [enrollment for enrollment in self.enrollments if enrollment.course.course_id != course_id]
            del self.courses[course_id]
        else:
            print(f"Course with ID {course_id} not found.")

    def update_course(self, course_id, course_name=None) -> None:
        """
        Function to update course object in LMS
        :param course_id: course_id string
        :param course_name: course_name string
        """
        if course_id in self.courses:
            course = self.courses[course_id]
            if course_name:
                course.course_name = course_name
        else:
            print(f"Course with ID {course_id} not found.")

    # Enrollment management methods
    def enroll_student(self, id_number:str, course_id:str) -> None:
        """
        Function to enrole sttudent in specific course
        :param id_number: id_number of person string
        :param course_id: course_id string
        """
        if id_number in self.students and course_id in self.courses:
            student = self.students[id_number]
            course = self.courses[course_id]
            course.add_student(student)
            enrollment = Enrollment(student=student, course=course)
            self.enrollments.append(enrollment)
        else:
            print(f"Student ID Number {id_number} or Course ID {course_id} not found.")

    def assign_grade(self, id_number:str, course_id:str, grade:str)->None:
        """
        Function to grade for specific course to student
        :param id_number: id_number of person string
        :param course_id: course_id string
        :param grade: grade string
        """
        for enrollment in self.enrollments:
            if enrollment.student.id_number == id_number and enrollment.course.course_id == course_id:
                enrollment.assign_grade(grade)
                return
        print(f"Enrollment not found for Student ID Number{id_number} in Course ID {course_id}.")

    # Retrieval methods
    def get_students_in_course(self, course_id:str) -> list:
        """
        Function to return list of students in specific course
        :param course_id: course_id string
        """
        if course_id in self.courses:
            course = self.courses[course_id]
            return course.enrolled_students
        else:
            print(f"Course with ID {course_id} not found.")
            return []

    def get_courses_for_student(self, id_number:str) -> list:
        """
        Function to return list of courses a student attends
        :param id_number: id_number of person
        """
        if id_number in self.students:
            student_courses = [enrollment.course for enrollment in self.enrollments if enrollment.student.id_number == id_number]
            return student_courses
        else:
            print(f"Student with ID Number {id_number} not found.")
            return []
