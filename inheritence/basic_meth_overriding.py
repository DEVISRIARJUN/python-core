#basic overriding
class A:
    def m1(self):
        print("m1 A class")
class B(A):
    def m1(self):
        print("m1 B class")
a=A()
b=B()
a.m1()
b.m1()