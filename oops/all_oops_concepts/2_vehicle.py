# 2. Build:
# • Vehicle base class
# • Car, Bike, Auto subclasses
# • A Driver class that contains a Vehicle
# • A Ride class that:
# o Calculates fare differently depending on the type of vehicle (polymorphism)
# o Stores driver + vehicle combination
# o Protects internal fare formula through encapsulation
# Also:
# • Use __str__ to print readable ride summaries.



class Vehicle:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number
    def calculate_fare(self, distance):
        pass
class Car(Vehicle):
    def calculate_fare(self, distance):
        return distance * 20
class Bike(Vehicle):
    def calculate_fare(self, distance):
        return distance * 10
class Auto(Vehicle):
    def calculate_fare(self, distance):
        return distance * 15
class Driver:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle
class Ride:
    def __init__(self, driver, distance):
        self.driver = driver
        self.vehicle = driver.vehicle
        self.distance = distance
        self.__fare = self.__calculate_fare()
    def __calculate_fare(self):
        return self.vehicle.calculate_fare(self.distance)
    def get_fare(self):
        return self.__fare
    def __str__(self):
        return (f"Driver: {self.driver.name}, "
                f"Vehicle: {self.vehicle.__class__.__name__}, "
                f"Vehicle Number: {self.vehicle.vehicle_number}, "
                f"Distance: {self.distance} km, "
                f"Fare: ₹{self.__fare}")
car = Car("CAR101")
bike = Bike("BIKE202")
auto = Auto("AUTO303")
driver1 = Driver("Arjun", car)
driver2 = Driver("Ravi", bike)
driver3 = Driver("Kiran", auto)
ride1 = Ride(driver1, 10)
ride2 = Ride(driver2, 10)
ride3 = Ride(driver3, 10)
print(ride1)
print(ride2)
print(ride3)