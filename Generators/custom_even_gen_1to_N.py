# 2) 2.	Write a generator that yields even numbers from 1 to N

def even(n):
    for i in range(1,n+1):
        if i % 2 == 0:
            yield i 
n = 10
for num in even(n):
    print(num)