#  Create a class LoginSystem with a method login(password) that raises an exception for an incorrect password and handles the exception outside the class.


class LoginSystem:
    def login(self,password):
        if password != "1234":
            raise Exception("Please enter correct password")
        print("logged in sucessfully")
l = LoginSystem()
try:
    l.login("6789")
except Exception as e:
    print("Error caught :",e)