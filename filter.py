#Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
# filter() to keep only the keys whose values are greater than 50.

# d = {"apple": 100, "banana": 40, "cherry": 150}
# k = list(filter(lambda x : d[x]>50 ,d))
# print(k)

# m = list(filter(lambda x : x > 50,d.values()))
# print(m)



#  Use filter() to remove all vowels from a string and print the final string.

# s = "bommisetty devi sri arjun"
# m = list(filter(lambda x : x not in "aeiouAEIOU",s))
# print(m)
# a = "".join(m)
# print(a)



#Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use filter() to keep only the keys whose values are greater than 50.

# d = {"apple": 100, "banana": 40, "cherry": 150}

# result = dict(filter(lambda item: item[1] > 50, d.items()))

# print(result)





# Given a list of numbers:
# [5, 10, 15, 20, 25, 30]
# Perform the following in a single pipeline:
# • Use map() to square each number
# • Use filter() to keep only numbers divisible by 5
# • Use reduce() to calculate the sum of remaining numbers


# from functools import reduce
# l = [5, 10, 15, 20, 25, 30]
# k = reduce(lambda x,y:x+y,filter(lambda x:x % 5 == 0,map(lambda x : x**2,l)))
# print(k)
