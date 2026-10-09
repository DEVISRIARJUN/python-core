# • Create a class Student with an attribute marks. Implement a method
# set_marks(marks) that raises a ValueError if marks are not in the range 0 to
# 100.

class Student:
    def __init__(self,marks):
        self.marks = marks
    def set_marks(self,marks):
        if marks < 0 or marks  > 100:
            raise ValueError("marks should be from 1 to 100")
        self.marks = marks
s = Student(50)
s.set_marks(101)
print(s.marks)