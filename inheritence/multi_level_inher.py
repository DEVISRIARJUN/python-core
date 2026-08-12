# Multilevel inheritance 

class Users:
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob
    def login(self):
        print("login sucessfully")
    def logout(self):
        print("logout sucessfully")
class Student(Users):
    def exams(self):
        print("Exams attended")
class Teacher(Student):
    def explaining(self):
        print("Teached today class sucessfully")
s1 = Teacher("salar","25-11-1978")
s1.exams()
