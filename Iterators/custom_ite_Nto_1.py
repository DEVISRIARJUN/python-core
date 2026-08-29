#  2) Create an custom iterator that prints numbers from N to 1.

class Number:
    def __init__(self,num):
        self.num = num
        self.i = num
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= 1:
            k = self.i
            self.i = self.i - 1
            return k
        else:
            raise StopIteration
n = int(input())
dec = Number(n)
for i in dec:
    print(i)
