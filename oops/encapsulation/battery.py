class SmartPhone:
    def __init__(self):
        self.__battery = 50  
    # Public way to view battery  @property , @battery.setter
    def check_battery(self):
        return f"Battery is at {self.__battery}%"
    # Public way to change battery safely
    def charge(self, amount):
        if amount > 0:
            self.__battery = min(100, self.__battery + amount)
phone = SmartPhone()
phone.charge(30)
print(phone.check_battery())  # Output: Battery is at 80%