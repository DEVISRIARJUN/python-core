#  Q9. Create a function draw(shape) that works for objects of classes Circle, Square, and
# Rectangle,
# each implementing a draw() method.
# Add another unrelated class Car with draw() and pass it — what happens and why?

def drawn(shape):
    shape.draw()
class Circle:
    def draw(self):
        print("Circle drawn")
class Square:
    def draw(self):
        print("Square drawn")
class Rectangle:
    def draw(self):
        print("Rectangle drawn")
class Car:
    def draw(self):
        print("Circular car")
shapes = [Circle(),Square(),Rectangle(),Car()]
for shap in shapes:
    drawn(shap)


