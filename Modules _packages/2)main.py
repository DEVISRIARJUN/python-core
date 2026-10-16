
# 2. Create a Python package that contains two or more modules. Each module should define classes with attributes and methods. Then create another module outside the package, import the package modules, and create a subclass that inherits from at least one of the classes. Finally, create objects of both parent and child classes.



from mixed_topics import Person,Student



class College_student(Person):
    def __init__(self,name,age,roll_number,subject):
        super().__init__(name,age)
        self.roll_number = roll_number
        self.subject = subject
    def display_details(self):
        self.display_person()
        print("Roll number :",self.roll_number)
        print("Subject :",self.subject)

                
p = Person("Arjun",21)
print("Parent file")
p.display_person()
print()

s = Student(1234567,"maths")
print("child_file")
s.display_student()
print()

c = College_student("Arjun",21,1234567,"maths")
print("Main_file")
c.display_details()



