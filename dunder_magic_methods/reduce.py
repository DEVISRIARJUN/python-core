# l = [1,3,2,5,6,3]
# from functools import reduce
# k = reduce(lambda x,y:x+y,l,2026)
# print(k)

# l = [1,2,3,5]
# from functools import reduce
# m = reduce(lambda x,y:x+y,[],20)
# print(m)


#Use functools.reduce() with a lambda to find the largest number from a given list Dynamically.
# from functools import reduce
# l = [10,20,30,40,50,60]
# m = reduce(lambda a , b : a if a > b else b,l)
# print(m)



#What happens if the lambda passed to reduce() accepts only one parameter or three parameters? Explain the output or error.
# from functools import reduce
# l = [1,2,3,4,5]
# m = reduce(lambda x,y,z : x + y + z,l)
# print(l)

#it shows the type error TypeError: <lambda>() missing 1 required positional argument: 'z'




# Use reduce() to concatenate a list of characters into a single string. Example input: ['P', 'y', 't', 'h', 'o', 'n'].

# from functools import reduce
# concat = ["p","y","t","h","o","n"]
# m = reduce(lambda x,y:x+y,concat) 
# print(m)



# from functools import reduce
# list = [10,20,30,40,50]
# result = reduce(lambda x,y : x if x > y else y,list)
# print(result)

