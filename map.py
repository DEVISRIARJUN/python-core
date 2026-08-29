# Use map() on a string to convert each character into its ASCII value (using ord()). Print the result list.

# s = "arjun"
# m = list(map(lambda x : ord(x),s))
# print(m)




#   #  Given a list of integers, use map() with id() to print the memory address
# of each element. Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.

# m = [10,350,10,350,20]
# l = list(map(lambda x : id(x),m))
# print(l)


#Use map() to square each number
# n = [1,2,3,4,5,6,7,8,9]
# k = list(map(lambda x : x * x,n))
# print(k)


# Given two lists:
# a = [1, 2, 3, 4] b = [10, 20, 30, 40]
# Use map() with a lambda to create a new list containing the sum of corresponding
# elements.
# What happens if the lists are of unequal length?  --->if lengths are unequal it ignore that element

a = [1,2,3,4]
b = [10,20,30,40]
k = list(map(lambda x,y : x + y,a,b))
print(k)

