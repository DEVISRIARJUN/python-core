#Inheritance introduction in python oops
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
class Teacher(Users):
    def explaining(self):
        print("Teached today class sucessfully")
s1 = Student("salar","25-11-1978")
s1.exams()
s1.login()
s1.logout()
s2 = Teacher("Snthosh","15-12-2001")
s2.explaining()

