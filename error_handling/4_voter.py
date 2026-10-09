# • Create a custom exception named InvalidAgeError. Create a class Voter with a
# method check_eligibility(age) that raises this exception if age is less than 18.


class InvalidAgeError(Exception):
    pass
class Voter:
    def check_eligibility(self,age):
        if age < 18:
            raise InvalidAgeError("voter should be above 18")
        self.age = age
v = Voter()
v.check_eligibility(16)
print(v.age)
