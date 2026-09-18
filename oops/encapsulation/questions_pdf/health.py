# 6. Create a Character class with:
# • private _health
# • methods to damage(points) and heal(points)
# • health cannot drop below 0 or exceed max limit
# • expose only current health through a read-only getter


class Charecter:
    def __init__(self,name):
        self.name = name
        self.__health = 100
    def damage(self,p,obj):
        if obj.__health > p:
            obj.__health -= p
        else:
            obj.__health = 0
    def heal(self,p):
        if self.__health + p < 100:
            self.__health += p
        else:
            self.__health = 100
    def get_health(self):
        return self.__health
c1 = Charecter("nikhil")
c2 = Charecter("arjun")
c1.damage(20,c2)
print(c1.get_health())
