# 10. Create a class using @property and @setter for a private attribute.
# Then:
# 1. Show correct usage
# 2. Show how forgetting to use underscore prefix breaks encapsulation
# 3. Show what happens if you implement a setter without validation


class A:
    def __init__(self):
        self.__x = 5
    @property
    def k(self):
        return self.__x
    @k.setter
    def z(self,nx):
        if nx < 10 and nx > 0:
            self.__x = nx
obj = A()
print(obj.k)#5
obj.z = 15
print(obj.k)#5
obj.z = 9
print(obj.k)#9