# 13. Create:
# • Abstract class VehicleControl with methods accelerate(), brake(), steer()
# • Implement CarControl, BikeControl, TruckControl


from abc import ABC,abstractmethod
class VehicleControl(ABC):
    @abstractmethod
    def accelerate(self):
        pass
    def brake(self):
        pass
    def steer(self):
        pass
class CarControl(VehicleControl):
    def accelerate(self):
        print("Acclearate slowly while on the main road")
    def brake(self):
        print("Break is very important on going with the speed ")
    def steer(self):
        print("Car is steering")
class BikeControl(VehicleControl):
    def accelerate(self):
        print("Bike is accelerating")
    def brake(self):
        print("Bike is braking")
    def steer(self):
        print("Bike is steering")
class TruckControl(VehicleControl):
    def accelerate(self):
        print("Truck is accelerating")
    def brake(self):
        print("Truck is braking")
    def steer(self):
        print("Truck is steering")
# Single interface
vehicles = [CarControl(), BikeControl(), TruckControl()]
for vehicle in vehicles:
    vehicle.accelerate()
    vehicle.brake()
    vehicle.steer()
    print()