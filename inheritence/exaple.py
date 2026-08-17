# create a base class A with m1 and m2 methods and subclass B with m3 method, 
# create a object for  both the class and call the methods
class A:
    def m1(self):
        print("Method 1")
    def m2(self):
        print("Method 2")
class B(A):
    def m3(self):
        print("Method 3")
d1 = A()
d1.m1()
d1.m2()
d2 = B()
d2.m3()
d2.m1()
d2.m2()    








                                                                                                                                                                                                                                                                                                                      