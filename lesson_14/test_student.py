
import pytest
from lesson_14.student import Student

def test_update_grade():
    student = Student("Jorj", "Redil", 20, 86.3)
    student.update_grade(96.7)
    assert student.average_grade == 96.7

def test_str():
    student = Student("Jorj", "Redil", 20, 86.3)
    assert str(student) == "Student: Jorj Redil, Age: 20, Average Grade: 86.3"

if __name__ == "__main__":
    pytest.main()