


# Write a simple decorator called my_decorator that prints 'Function is starting' before
# and 'Function is done' after any function it wraps. Apply it to a function greet() that prints
# 'Hello!'.


# def my_decorator(func):
#     def inner(n):
#         print("function is starting")
#         func(n)
#         print("function is done")
#     return inner
# @my_decorator
# def greet(name):
#     print(f"{name}")
# print(greet.__name__)
# greet("Hello")


def ann(func):
    def inner(x,y):
        print(x,y)
        return func(x,y)
    return inner
@ann
def fun(a:int,b:int) ->int:
    """just adding a doc fro teh function"""
    return a + b
print(fun(a:10,b:24))
print(fun.__name__)
print(fun(a:10,b:24))