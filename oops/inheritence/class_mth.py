#using class method in the inheritance


class A:
    @classmethod
    def m2(cls):
        print("Hello")
    @classmethod
    def m3(self):
        print("Bye")
    def m4(self):
        print("Just Demo")
class B:
    @classmethod
    def m2(cls):
        print("World")
        a1 = A()   #composition means what type of the method you want to use you will call it in the 
        a1.m4()    # 
        # super().m3()
b1 = B()
b1.m2()
