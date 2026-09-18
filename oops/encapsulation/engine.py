# 7. Create:
# • An Engine class with private state like temperature
# • A Car class that uses an Engine but should:
# o Not allow users to manipulate engine temperature
# o Only expose methods like start_car() or cool_engine()



class Engine:
    def __init__(self,type):
        self.type = type
        self.temp = 32
    def cool_engine(self):
        self.__temp -= 10
    def start_engine(self):
        print("Started engine")
        self.__temp += 10
class Car:
    def __init__(self,brand,engine):
        self.brand = brand
        self.engine = engine
    def start_engine(self):
        self.engine.start_engine()
    def stop_car(self):
        self.engine.cool_engine()
c1 = Car("bmw",Engine("v12"))
