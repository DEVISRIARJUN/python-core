#  1.	Write a generator that yields numbers from 1 to N.

def numbers(n):
    for i in range(1,n+1):
        yield i
n = 5
for num in numbers(n):
    print(num)