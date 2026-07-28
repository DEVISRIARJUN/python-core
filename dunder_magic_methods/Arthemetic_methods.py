#Dunder Arthemetic methods
class A:
    def __init__(self,x):
        self.x = x
    def __add__(self,y):
        return self.x+y.x
    def __sub__(self,z):
        return self.x-z.x
a1 = A(20)
a2 = A(30)
print(a1+a2)
print(a1-a2)