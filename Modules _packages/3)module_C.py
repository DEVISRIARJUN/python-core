# 5. Create three modules: Module A: class Animal Module B: class Walkable Module C: class Dog that inherits from both Animal and Walkable Demonstrate method resolution order (MRO) by calling overridden methods and printing the MRO.

from three_modules import Animal,Walkable

class Dog(Animal,Walkable):
    def __init__(self,name,power,man,dog):
        super().__init__(name,power)
        super().__init__(man,dog)
    def display_main(self):
        self.display_modA()
        self.display_modB()
a = Animal("Tiger","Hunting")
a.display_modA()

w = Walkable("Yes","Four legs")
w.display_modB()


