class Even:
    def __init__(self,l):
        self.l = l
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.l):
            n = self.l[self.index]
            self.index += 1
            if n % 2 == 0:
                return n
            # else:
            #     return next(self)    #recursion
        else:
            raise StopIteration
e = Even([1,4,67,68,35,57,54])
for i in e:
    print(i)