
# def dec(h):
#     def inner(n):
#         print("start")
#         print(h.__name__)
#         h(n)
#     return inner
# @dec
# def greet(name):
#     print(f"hello {name}")
# print(greet.__name__)
# greet("arjun")


# def login(func):
#     def inner():
#         un = input()
#         pasw = input()
#         if un == "arjun" and pasw == "123":
#             return func()
#         else:
#             return "Invalid Credentials"
#     return inner
# @login
# def secretfile():
#     return "secrectfile"
# print(secretfile())



# def valid(func):
#     def inner(x,y):
#         if isinstance(x,int) and isinstance(y,int):
#             print(f"multiply of {x} and {y} is :",end="")
#             func(x,y)
#         else:
#             print("Given inputs is not integers")
#     return inner
# @valid
# def multiply(x,y):
#      print(x*y)
# multiply(6,8)

# Write a simple decorator called my_decorator that prints 'Function is starting' before
# and 'Function is done' after any function it wraps. Apply it to a function greet() that prints
# 'Hello!'.



# def my_decorator(fun2):
#     def inner():
#         print("Function is starting")
#         fun2()
#         print("Function is done")
#     return inner
# @my_decorator
# def greet():
#     print("hello")
# greet()






# Write a decorator called validate_positive that checks all positional arguments passed
# to a function. If any argument is negative, print an error message and return None without
# calling the function. Test it on a function multiply(a, b).


# def validate_positive(fun2):
#     def inner(*args):
#         for num in args:
#             if num < 0:
#                 print("Error the number is less than zero")
#                 return None
#         return fun2(*args)
#     return inner

# @validate_positive
# def multiply(a,b):
#     return a*b
# print(multiply(2,3))
# print(multiply(-2,3))


