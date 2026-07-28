# vector _add__ two variables x and y


class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,any):
        return (self.x+any.x,self.y+any.y)
    def __sub__(self,any):
        return (self.x-any.x,self.y-any.y)
    def __mul__(self,any):
        return (self.x*any.x,self.y*any.y)
    def __truediv__(self,any):
        return (self.x/any.x,self.y/any.y)
    def __mod__(self,any):
        return (self.x%any.x,self.y%any.y)
v1 = Vector(20,30)
v2 = Vector(15,10)
print(v1+v2)
print(v1-v2)
print(v1*v2)
print(v1/v2)
print(v1%v2)