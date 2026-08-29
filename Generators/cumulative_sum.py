# Write a program for yield to generate a sum of cumulative numbers.

def cumulative(n):
    sum = 0
    for i in n:
        sum = sum + i
        yield sum
n = [1,2,3,4,5,6,7,8,9,10]
for i in cumulative(n):
    print(i)