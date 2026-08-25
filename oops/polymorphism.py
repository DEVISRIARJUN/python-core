# polymorphism in the python program is one of the oops concept 
# the name poly means many and the morphism means forms . by using the same method(behaviour) 
# we can create multiple classes in the different forms.

class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")

animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()