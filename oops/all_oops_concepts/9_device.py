# 9. Classes:
# • LightDevice
# • SecurityDevice
# • SmartCamera(LightDevice, SecurityDevice)
# Requirements:
# • Resolve method conflicts using MRO
# • Encapsulate internal camera logs
# • SmartCamera overrides both parents’ behaviors
# • Use super() responsibly in multiple inheritance



class LightDevice:
    def on(self):
        print("Light is on")
        super().on()
    def off(self):
        print("Light is off")
        super().off()
class SecurityDevice:
    def on(self):
        print("Devise is on")
    def off(self):
        print("Devise is off")
class SmartCamera(LightDevice,SecurityDevice):
    def on(self):
        print("Camera is on")
        super().on()
    def off(self):
        print("Camera is off")
        super().off()
    def __logs(self):
        print("logged into the data sucessfully")
    def show_logs(self):
        if input("Enter the password") == "12345":
            return self.__logs()
s = SmartCamera()
s.on()
s.off()
s.show_logs()