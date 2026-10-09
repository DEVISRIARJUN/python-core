#  Create a class PasswordValidator with a method validate(password). Raise an exception if the password length is less than 8 characters.


class Passwordvalidator:
    def validate(self,password):
        if len(password) < 8:
            raise Exception("Th length of the passowrd is invalid")
        print("Logged sucessfully")
p = Passwordvalidator()
p.validate("1ah568h8")     