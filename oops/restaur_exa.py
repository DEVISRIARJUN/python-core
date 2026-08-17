# create a class land_animal with method being create a class water_animal with method
# water and create a subclass frog that inherits both the classes with method living that calls both being and and water methods.


class LandAnimal:
    def being(self):
        print("Being in the forest")
class WaterAnimal:
    def water(self):
        print("Water animal")
class Frog(LandAnimal,WaterAnimal):
    def living(self):
        self.being()
        self.water()
        print("I can live in both the land and water")
# L = LandAnimal()
# W = WaterAnimal()
F = Frog()
F.living()