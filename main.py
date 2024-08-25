from person import Person
from student import Student
from instructor import Instructor
from course import Course
from enrollment import Enrollment
from studentManagementSystem import StudentManagementSystem

if __name__ == "__main__":
    # Create instances of Person, Student, Instructor, Course, and Enrollment
    student1 = Student(name="Alice", id_number="S12345", major="Computer Science")
    student2 = Student(name="Bob", id_number="S67890", major="Mathematics")

    instructor1 = Instructor(name="Dr. Smith", id_number="E67890", department="Computer Science")

    course1 = Course(course_name="Introduction to Python", course_id="C101")
    course2 = Course(course_name="Data Structures", course_id="C102")

    # Initialize Student Management System
    sms = StudentManagementSystem()

    # Add entities
    sms.add_student(student1)
    sms.add_student(student2)
    sms.add_instructor(instructor1)
    sms.add_course(course1)
    sms.add_course(course2)


    # Enroll students
    sms.enroll_student("S12345", "C101")
    sms.enroll_student("S67890", "C102")

    # Assign grades
    sms.assign_grade("S12345", "C101", "A")
    sms.assign_grade("S67890", "C102", "B+")

    # sms.get_students_in_course("C101")

    # print("Students in 'Introduction to Python':")
    # for student in sms.get_students_in_course("C101"):
    #     print(student.name)




    print(student1.name)
    print(instructor1.name)
    print(course1.course_name)
    print(sms.enrollments)
    print(sms.courses)
    print(sms.students)
    print(sms.get_students_in_course("C101"))
