# single inheritance


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
class Instagram(User):
    def post(self):
        print(f"{self.name} post")
        print("Got 1L likes")
i = Instagram("Arjun",21,"Male","23 jul 2005")
i.login()
i.logout()
i.post()