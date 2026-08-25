#method overloading fails

class A:
    def hello(self,a,b):
        return a+b
    def hello(self,a,b,c):
        return a+b+c
res = A()
print(res.hello(10,20,30))


#we can acheive the method overloading by using the default arguments or *args

class A:
    def hello(self,*args):
        return sum(args)
res = A()
print(res.hello(10,20,30))
print(res.hello(10,20,30,40,50))


