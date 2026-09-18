# 3. Create a SecureFile class that:
# • stores content privately
# • provides a method read(password)
# • refuses access if the password is incorrect
# • logs an "Unauthorized attempt" internally (cannot be accessed from outside)



class SecureFile:
    def __init__(self,password,content):
        self.__password = password
        self.__content = content
        self.__log = []
    def read(self,password):
        if password == self.__password:
            print("Content :",self.__content)
        else:
            self.__log.append("Unauthrized attempt")
            print("Incorrect password")
    def show_log(self):
        print(self.__log)
s = SecureFile(1234,"This File is Secured")
s.read(1234)
s.read(2345)
s.show_log()
print(s.__log)