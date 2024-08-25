## Overview

The Student Management System (SMS) is a Python-based system designed to manage students, instructors, courses, and enrollments. The system provides functionality to add, remove, and update records, enroll students in courses, assign grades, and retrieve lists of students or courses.

## Features

- **Student Management**
  - Add new students
  - Remove existing students
  - Update student details

- **Instructor Management**
  - Add new instructors
  - Remove existing instructors
  - Update instructor details

- **Course Management**
  - Add new courses
  - Remove existing courses
  - Update course details

- **Enrollment Management**
  - Enroll students in courses
  - Assign grades to students
  - Retrieve a list of students enrolled in a specific course
  - Retrieve a list of courses a specific student is enrolled in

## Usage

To use the Student Management System, create an instance of `StudentManagementSystem` and use the provided methods to manage students, instructors, courses, and enrollments.

### Example

```python
# Create an instance of the Student Management System
sms = StudentManagementSystem()

# Add a student
student = Student(name="Alice", age=20, student_id="S12345", major="Computer Science")
sms.add_student(student)

# Add a course
course = Course(course_name="Introduction to Python", course_id="C101")
sms.add_course(course)

# Enroll the student in the course
sms.enroll_student(student, course)

# Assign a grade to the student
sms.assign_grade(student, course, "A")

# Retrieve and print the list of students in the course
students_in_course = sms.get_students_in_course("C101")
print(students_in_course)

# Retrieve and print the list of courses the student is enrolled in
courses_for_student = sms.get_courses_for_student("S12345")
print(courses_for_student)
