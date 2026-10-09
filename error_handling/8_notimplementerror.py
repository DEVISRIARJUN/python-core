
#  Create a base class Shape with a method area() that raises NotImplementedError. Create a child class Rectangle that overrides and implements the area method.


class Shape:
    def area(self):
        raise NotImplementedError()
class Rectangle(Shape):
    def area(self):
        print("Rectancgle shape")
    
r = Rectangle()
r.area()


