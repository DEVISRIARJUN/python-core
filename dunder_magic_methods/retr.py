class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f"position at ({self.x},{self.y})"
    def __repr__(self):
        return f"({self.x},{self.y})"
v1 = Vector(10,20)
v2=Vector(20,30)
print(v1)
print(v2)
l=[v1,v2]
print(l)
