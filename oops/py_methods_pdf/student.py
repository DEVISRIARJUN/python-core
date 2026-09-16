# ## Q1. Create a class Student that:
# •	Keeps track of the total number of students created.
# •	Determines whether a student passed or failed based on a shared passing mark.
# •	Provides a method to curve marks by increasing everyone’s marks by a percentage.
# •	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).

class Student:
    total_students = 0
    pass_marks = 35
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1
    def result(self):
        if self.marks >= self.pass_marks:
            print("Passed")
        else:
            print("Failed")
    @staticmethod
    def grade(marks):
        if marks >= 90:
            print("A grade")
        elif marks >= 80:
            print("B grade")
        elif marks >= 70:
            print("C grade")
        elif marks >= 60:
            print("D grade")
        elif marks >= 35:
            print("E grade")
        else:
            print("Fail")
print("Student1")
s1 = Student("Arjun",95)
print(s1.name)
print(s1.marks)
s1.result()
Student.grade(s1.marks)
print()
print("Student 2")
s2 = Student("Deva",34)
print(s2.name)
print(s2.marks)
s2.result()
Student.grade(s2.marks)