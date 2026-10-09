#  Create a class UserInput with a method get_integer(value). Handle ValueError and TypeError using separate except blocks.

class UserInput:
    def get_integer(self, value):
        try:
            num = int(value)
            print("Integer:", num)
        except ValueError:
            print("ValueError: Please enter a valid integer.")
        except TypeError:
            print("TypeError: The value cannot be converted to an integer.")
u = UserInput()
u.get_integer("123")
u.get_integer("abc")
u.get_integer(None)






