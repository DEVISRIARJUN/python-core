
#Classes Basic Program

# class Ticket:
#     source = "Vijayawada"
#     destiantion = "Hyderabad"
#     total = 0
#     def __init__(self,name,age,email,phonenumber):
#         self.name = name
#         self.age = age
#         self.email = email
#         self.phonenumber = phonenumber
#         Ticket.total += 1
# t1 = Ticket("arjun",21,"devisriarjun@12gamil.com",123434)
# print(t1.name)
# print(t1.__dict__)


# Create a class Student with instance attributes name and marks. Add an instance method is_passed() that return True if marks > 40. Then create 2 student objects and print whether each has passed or failed.

# def new_func():
#     class Student:
#         def __init__(self,name,marks):
#             self.name = name
#             self.marks = marks
#         def is_passed(self):
#             return self.marks > 40
#     s1 = Student("Arjun",100)
#     s2 = Student("praveen",30)
#     if s1.is_passed():
#         print(s1.name,"passed")
#     else:
#         print(s1.name,"fail")
#     if s2.is_passed():
#         print(s2.name,"passed")
#     else:
#         print(s2.name,"fail")
#     print(s1.is_passed())
#     print(s2.is_passed())

# return new_func()


# Q2. Create a class Employee with attributes name and company_name = "TechCorp". Add a class method change_company
# (cls, new_name) to update the company name for all employees. Demonstrate how this change affects all instances.


# class Employee:
#     company_name = "TechCorp"
#     def __init__(self,name):
#         self.name = name
#     @classmethod
#     def change_company(cls,new_name):
#         cls.company_name = new_name
# e1 = Employee("ARJUN")
# e2 = Employee("Deva")
# Employee.change_company("GotiilaFactorypvt.limited")
# print(e1.name,e1.company_name)



#Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
#Then call it both from the class and an instance.

# class Mathops:
#     @staticmethod
#     def is_even(num):
#         if num % 2 == 0:
#             return True
#         else:
#             return False
# c = Mathops()
# print(Mathops.is_even(2))
# print(Mathops.is_even(5))



# Q4. Create a class Car with:
# •	instance attribute mileage
# •	class attribute wheels = 4
# Add an instance method display_specs() that prints mileage and wheels.
# Then change wheels using a class method, and print again.

# class Car:
#     wheels = 4
#     def __init__(self,mileage):
#         self.mileage = mileage
#     def display_specs(self):
#         print(self.mileage)
#         print(Car.wheels)
#     @classmethod
#     def update(cls,new):
#         cls.wheels = new
# c = Car(150)
# Car.update(6)
# c.display_specs()



# Q5. Create a class Temperature with:
# •	instance attribute celsius
# •	a static method to_fahrenheit(celsius)
# •	an instance method show_conversion() that uses the static method to print both values.

# class Temp:
#     def __init__(self,celsius):
#         self.celsius = celsius
#     @staticmethod
#     def to_fahrenheit(celsius):
#         return (celsius * 9/5)+32
#     def show_conversion(self):
#         print(self.celsius)
#         print(Temp.to_fahrenheit(self.celsius))
# n=Temp(23)
# n.show_conversion()
 

# Q6. Create a class Book with:
# •	instance attributes title, author
# •	a class variable total_books
# •	a class method from_string(cls, book_str) that creates an object from "title-author" format
# •	a static method is_valid_title(title) that checks if title has at least 3 characters
# •	increment total_books for every book created


# class Book:
#     total_books = 0
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
#         Book.total_books = Book.total_books + 1
#     @classmethod
#     def from_strings(cls,book_str):
#         title,author = book_str.split("-")
#         if cls.valid(title):
#             b = Book(title,author)
#             return b
#         else:
#             return "Invalid Title" 
#     @staticmethod
#     def valid(title):
#         return len(title) > 3
# b1 = Book("Bhagavadgeetha","SriKrishna")
# b2 = Book.from_strings("Wings of Arts-APJ Abdul Kalam")      
# print(b2.__dict__)   


# Q7. Create a class Employee with:
# •	instance attributes: name, base_salary
# •	class variable: bonus_rate = 0.1
# •	instance method: final_salary() → base_salary + (base_salary × bonus_rate)
# •	class method: update_bonus(cls, new_rate) → updates bonus for all employees
# •	static method: is_valid_salary(sal) → checks if salary > 0

# class Employee:
#     bonus_rate = 0.1
#     def __init__(self,name,base_salary):
#         self.name = name
#         self.base_salary = base_salary
#     def final_salary(self):
#         return self.base_salary + (self.base_salary * Employee.bonus_rate)
#     @classmethod
#     def update_bonus(cls,new_rate):
#         cls.bonus_rate = new_rate
#     @staticmethod
#     def is_valid_salary(sal):
#         return sal > 0
# e1 = Employee("Praveen",100000)
# e2 = Employee("Arjun",250000)
# print("Befor Bonus update")
# print(e1.name,e1.final_salary())
# print("After bonus update")
# Employee.update_bonus(0.2)
# print(e1.name,e1.final_salary())
# print("Salary Validation")
# print(Employee.is_valid_salary(60000))
# print(Employee.is_valid_salary(-15000))



# Q8. Create a class Course with:
# •	class variable total_students
# •	instance variable student_name
# •	instance method enroll() → increments total_students
# •	class method show_total(cls) → prints total students
# •	static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count.

# class Course:
#     total_students = 0
#     def __init__(self,student_name):
#         self.student_name = student_name
#     def enroll(self):
#         Course.total_students = Course.total_students + 1
#     @classmethod
#     def show_total(cls):
#         print(cls.total_students)
#     @staticmethod
#     def is_eligible(age):
#         return age >= 18       
# c1 = Course("Arjun")
# c2 = Course("Nikhil")
# print(c1.student_name)
# c1.enroll()
# print(c2.student_name)
# c2.enroll()
# Course.show_total()
# print(Course.is_eligible(20))
# print(Course.is_eligible(17))



# Q9. Create a class BankAccount with:
# •	class variable bank_name
# •	instance variables holder and balance
# •	instance method deposit(amount)
# •	class method change_bank_name(cls, new_name)
# •	static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together.


# class BankAccount:
#     bank_name = "bandhan"
#     def __init__(self,holder,balance):
#         self.holder = holder
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#     @classmethod
#     def change_bank_name(cls,new_name):
#         cls.bank_name = new_name
#     @staticmethod
#     def validate_amount(amount):
#         return amount > 0
# acc1 = BankAccount("Arjun",10000)
# acc1.deposit(1000)
# BankAccount.change_bank_name("Bank Of India")
# print(BankAccount.bank_name)


# Q10. Create a class Student with:
# •	class variable passing_marks = 40
# •	instance attributes name, marks
# •	instance method result() → prints pass/fail using class variable
# •	class method update_passing_marks(cls, new_marks)
# •	static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.	Creates students
# 2.	Updates the passing criteria
# 3.	Displays grade category and result

# class Student:
#     passing_marks = 40
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def result(self):
#         if self.marks > Student.passing_marks:
#             print("pass")
#         else:
#             print("fail")
#     @classmethod
#     def update_passing(cls,new_marks):
#         cls.passing_marks = new_marks
#     @staticmethod
#     def grade_category(marks):
#         if marks > 80:
#             return "A"
#         elif marks > 70:
#             return "B"
#         else:
#             return "C"
# s1 = Student("Arjun",36)
# s1.result()

# Student.update_passing(35)
# s1.result()
# print(Student.grade_category(s1.marks))







    





    
    

    


    


