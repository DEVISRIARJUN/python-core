#1)  Create a base class Animal with a method sound(). Create a derived class Dog that overrides the sound() method. Demonstrate method overriding.

# class Animal:
#     def sound(self):
#         print("I have some sound")
# class Dog(Animal):
#     def sound(self):
#         print("I will bark on the road")
# a = Animal()
# d = Dog()
# a.sound()
# d.sound()


# 2)  Create class A with method show(). Create class B(A) that overrides show() and also calls the parent method using super().

# class A:
#     def show(self):
#         print("Iam the parent class.")
# class B(A):
#     def show(self):
#         super().show()
#         print("Iam the child class")
# b = B()
# b.show()


# 3)  Create multi-level inheritance with classes A → B → C, each having a method display() printing the class name. Create object of C and call display(), showing method resolution.

# class A:
#     def display(self):
#         print("Hello")
# class B(A):
#     def display(self):
#         super().display()
#         print("Yes tell me")
# class C(B):
#     def display(self):
#         super().display()
#         print("Nothing tell me")
# c = C()
# c.display()


# 4) Implement hierarchical inheritance using a base class Vehicle and two child classes Car and Bike, each defining a method wheels().

# class Vehicle:
#     def wheels(self):
#         print("A vehicle has wheels")
# class Car(Vehicle):
#     def wheels(self):
#         print("A car has wheels")
# class Bike(Vehicle):
#     def wheels(self):
#         print("A bike has the wheels")
# b = Bike()
# b.wheels()
# c = Car()
# c.wheels()

#without using the wheels() in the car and bike class

# class Vehicle:
#     def __init__(self,n,no_of_wheels):
#         self.n = n
#         self.no_of_wheels = no_of_wheels
#     def wheels(self):
#         return self.no_of_wheels
# class Car(Vehicle):
#     def __init__(self,n):
#         super().__init__(n,4)
# class Bike(Vehicle):
#     def __init__(self,n):
#         super().__init__(n,2)
# c = Car("Maruthi")
# print(c.n)
# print(c.no_of_wheels)
# b = Bike("Splender")
# print(b.n)
# print(b.no_of_wheels)


# 5)  Create class Employee with an instance method salary(). Create class Manager(Employee) that overrides salary() and adds an incentive. Demonstrate both outputs.

# class Employee:
#     def salary(self):
#         return 20000
# class Manager(Employee):
#     def salary(self):
#         return super().salary() + 30000
# e = Employee()
# print(f"Employee salary :  {e.salary()}")
# m = Manager()
# print(f"Manager salary :  {m.salary()}")


# 6)  Create class University with a class variable and a class method. Inherit it into class College and access the parent’s class variable from the child class.

# class University:
#     name = "Amrita Sai"
#     @classmethod
#     def university(cls):
#         print("University name is :",cls.name)
# class College(University):
#     def college(self):
#         print("college name is",University.name)
# c = College()
# c.college()
# c.university()



    
#7) Create class MathOps with a static method add(a, b). Create class AdvancedOps(MathOps) and use the static method without overriding it.

# class Mathops:
#     @staticmethod
#     def add(a,b):
#         return a + b
# class AdvanceOps(Mathops):
#     pass
# print("Sum:",AdvanceOps.add(2,5))


# 8) Create two classes Father and Mother, both defining a method skills(). Create class Child(Father, Mother) and check which skills() runs using MRO.
 
# class Father:
#     def skills(self):
#         print("cooking")
#         super().skills()
# class Mother:
#     def skills(self):
#         print("Going")
# class Child(Father,Mother):
#     def skills(self):
#         print("Walking")
#         super().skills()
# c = Child()
# c.skills()


# 10) Create class Person with a constructor __init__(name). Create class Student(Person) with constructor __init__(name, roll). Use super() to call the parent constructor.

# class Person:
#     def __init__(self,name):
#         self.name = name
# class Student(Person):
#     def __init__(self,name,roll):
#         self.roll = roll
#         super().__init__(name)
#         print("My name is",self.name)
#         print("My number is",self.roll)
# s = Student("Arjun", 101)
# print("Name:", s.name)
# print("Roll:", s.roll)



