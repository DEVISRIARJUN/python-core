# class A:
#     def m1(self):
#         print("A class")
# class B(A):
#     def m1(self):
#         print("B class")
#         super().m1()
# b1 = B()
# b1.m1()
# print(B.mro())


# class User:
#     def order(self):
#         print("order pasta")
# class Restaurant(User):
#     def order(self):
#         super().order()
#         print("order Received")
# R1=Restaurant()
# R1.order()



class User:
    def order(self):
        print("order pasta")
class Restaurant(User):
    def order(self):
        super().order()
        print("order Received")
class Swiggy(Restaurant):
    def order(self):
        super().order()
        print("Delivary partner assigned")
s1 = Swiggy()
s1.order()
R1=Restaurant()
# R1.order()