#  Q2. Write a function operate(device) that calls device.start().
# Pass in objects of Car, Computer, and WashingMachine — all of which define a start()
# method, but share no inheritance relationship.
# Show that Python’s polymorphism works through behavior, not type.


def operate(device):
    device.start()
class Car:
    def start(self):
        print("Starting a car")
class Computer:
    def start(self):
        print("Turn on")
class Washingmachine:
    def start(self):
        print("Wasing")
k = [Car(),Computer(),Washingmachine()]
for i in k:
    operate(i)