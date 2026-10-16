class Student:
    def __init__(self,roll_no,subject):
        self.roll_no = roll_no
        self.subject = subject
    def display_student(self):
        print("Roll number :",self.roll_no)
        print("Subject :",self.subject)
        