#  Q3. Create a Vector class that supports: • + operator → add coordinates • == operator → compare equality Show how operator overloading gives natural polymorphism to user-defined classes. 


class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,o2):
        if isinstance(o2,Vector):
            return Vector(self.x+o2.x,self.y+o2.y)
        elif isinstance(o2,Vector)