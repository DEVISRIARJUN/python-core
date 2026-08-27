# Multiple inheritance is used for the creating the multiple classes using single parent class

# users class
#                \\\\\\\\\\\          
# chil1 class    \\\\\\\\\\\  parent class
#                \\\\\\\\\\\
# child2 class 


class User:
    def __init__(self,n,a,g,dob):
        self.name = n
        self.age = a
        self.gender = g
        self.date_of_birth = dob
    def login(self):
        print("Login sucessful")
    def logout(self):
        print("Logout sucessful")
class Restaurants:
    def __init__(self,name,rating,address):
        self.name = name
        self.rating = rating
        self.address = address
    def display_menu(self):
        print("All the dishes are veg only")
class Swiggy(User,Restaurants):
    def display(self):
        print("User details")
s1 = Swiggy("Arjun",21,"Male","23 jul 2005")
s1.login()
s1.display()
