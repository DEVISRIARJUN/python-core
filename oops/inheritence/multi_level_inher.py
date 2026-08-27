# Multilevel inheritance 

# class Users:
#     def __init__(self,name,dob):
#         self.name = name
#         self.dob = dob
#     def login(self):
#         print("login sucessfully")
#     def logout(self):
#         print("logout sucessfully")
# class Student(Users):
#     def exams(self):
#         print("Exams attended")
# class Teacher(Student):
#     def explaining(self):
#         print("Teached today class sucessfully")
# s1 = Teacher("salar","25-11-1978")
# s1.exams()



class Users:
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob
    def login(self):
        print("login sucessfully")
    def logout(self):
        print("logout sucessfully")
class Bank(Users):
    Name = "RBI"
    def guidelines(self):
        print("Beware of Scammer and call xxxxxx")
class BhimUPI(Bank):
    def payments(self,amount):
        print(f"{amount} has been paid paid through UPI")
b1 = BhimUPI("Arjun","22 july 2005")
b1.login()
b1.logout()
b1.guidelines()
b1.payments(50000)
print(BhimUPI.mro())
