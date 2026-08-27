# hierarchical inheritance


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
print(Swiggy.mro())
class Zomato(User,Restaurants):
    def display(self):
        print("user1 details")
class Customer(Swiggy,Zomato):
    def order(self):
        print("Just Ordering")
print(Customer.mro())
b1 = Zomato("Arjun",21,"Male","23 jul 2005")
b1.login()
b1.logout()
b1.display_menu()
b1.display()