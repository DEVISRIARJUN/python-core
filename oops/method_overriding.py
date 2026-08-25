# Method overriding means 

# A child class has a method with the same name as a method in the parent class, but the child provides its own implementation.

class A:
    def drink(self):
        print("Iam drinking the water")
class B(A):
    def drink(self):
        print("Iam drinking the coconut water")
        super().drink()
# res1 = A()
res2 = B()
# res1.drink()
res2.drink()