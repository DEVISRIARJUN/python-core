# 3) 3.	Create an custom iterator that prints the first N even numbers.
class Even:
    def __init__(self,num):
        self.num = num
        self.i = 2
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count < self.num:
            k = self.i
            self.i = self.i + 2
            self.count = self.count + 1
            return k
        else:
            raise StopIteration
n = int(input())
obj = Even(n)
for no in obj:
    print(no)