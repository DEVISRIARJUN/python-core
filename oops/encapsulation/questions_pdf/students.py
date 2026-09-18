# 2. Design a Student class where marks:
# • should always be between 0 and 100
# • should never be set directly
# Enable updating marks only through a controlled method that performs range
# checks.
# Demonstrate:
# • trying to assign marks manually
# • why encapsulation protects invalid states

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks
    def update_marks(self,marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
            print("marks :",marks)
        else:
            print("Invalid marks")
    def show_marks(self):
        print("Marks :",self.__marks)    
s = Student("Arjun",45)
s.update_marks(35)
s.show_marks()
