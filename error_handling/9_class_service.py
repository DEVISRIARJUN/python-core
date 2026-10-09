#  Create a class Service with a method that calls another method which raises an exception. Catch and handle the exception in the Service class.




class Service:
    def m1(self):
        try:
            self.m2()
        except Exception:
            raise Exception("By using the exception the error is handled")
    def m2(self):
        raise Exception("Calling the another method raises an Exception")
s = Service()
s.m1()