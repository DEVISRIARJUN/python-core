#  1. Create an custom iterator that prints numbers from 1 to N, where N is given by the user.

class Number:
    def __init__(self,num):
        self.num = num
        self.i = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.i <= self.num:
            k = self.i
            self.i = self.i + 1
            return k
        else:
            raise StopIteration
n = int(input())
obj = Number(n)
for num in obj:
    print(num)

