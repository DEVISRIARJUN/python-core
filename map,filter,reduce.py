# 1. Use map() with a lambda to add 5 to every element of the following nested
# l=[[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda k : k+[5],l))
# print(result)



#Given a list of numbers: [5, 10, 15, 20, 25, 30]    Use map() to square each number
# square = [5,10,15,20,25,30]
# k = list(map(lambda x:x ** 2,square))
# print(k)


# a = int(input())
# b = int(input())
# c = 0
# if a > 0 and b > 0:
    
#     if(a%2==0):
#         start=a+2
#     else:
#         start=a+1
#     for i in range(start,b+1,4):
#         if c > 0:
#             print(end = ", ")
#         print(i,end="")
#         c = c+1

# a = int(input())
# b = int(input())
# c = 0
# c1 = 0
# for i in range(a+1,b):
        
    
#         if (i % 2 == 0):
#             c = c + 1
#             if c%2==1:
#                 c1+=1
#                 if c1>1:
#                      print(end=",")
#                 print(i,end="")



#Given a list of numbers:
# [5, 10, 15, 20, 25, 30]
# Perform the following in a single pipeline:
# • Use map() to square each number
# • Use filter() to keep only numbers divisible by 5
# • Use reduce() to calculate the sum of remaining numbers


# from functools import reduce
# nums = [5, 10, 15, 20, 25, 30]
# result = reduce(lambda x, y: x + y,filter(lambda x: x % 5 == 0,map(lambda x: x * x, nums)))
# print(result)

# n = ["arjun","raheem","kaameshwararao"]
# k = sorted(n,key=len)
# print(k)

from functools import reduce
num = [1,2,3,4,5,6,7,8,90,10]
result = reduce(lambda x,y : x+y,filter(lambda x : x % 5 == 0,map(lambda x : x * 7,num)))
print(result)




















   
    