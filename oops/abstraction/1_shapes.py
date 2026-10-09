# 11. Using abc module:
# • Create an abstract class Shape with area(), perimeter()
# • Implement Circle, Rectangle, Triangle


from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s-self.a) * (s-self.b) * (s-self.c)) ** 0.5
    def perimeter(self):
        return self.a + self.b + self.c
c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(3, 4, 5)
print("Circle Area:", c.area())
print("Circle Perimeter:", c.perimeter())
print()
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())
print()
print("Triangle Area:", t.area())
print("Triangle Perimeter:", t.perimeter())
























