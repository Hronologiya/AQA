""" Create a class “Student” with attributes “first name”, “last name”, “age”, and “average grade”.
Create an object of this class representing a student.
Then add a method to the “Student” class that allows changing the student’s average grade.
Display the student’s information and change their average grade. """


class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_grade(self, new_grade):
        self.average_grade = new_grade

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, Age: {self.age}, Average Grade: {self.average_grade}"
