
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
