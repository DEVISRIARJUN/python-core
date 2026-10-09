# • Create a class Person whose constructor takes age as an argument. Raise a
# ValueError if the age is less than 0.


class Person:
    def __init__(self,age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.age = age
p = Person(-20)
print(p.age)