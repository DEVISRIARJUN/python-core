#double decorator

import functools
def ann(func):
    @functools.wraps(func)
    def inner(x,y):
        # print(func._name_)
        # print(func._annotations_)
        # print(func._doc_)
        print(x,y)
        return func(x,y)
    return inner


@ann
def fun(a:int,b:int) -> int:
    """Just adding a Doc for the function"""
    return a+b

print(fun(10,24))
print(fun.__name__)
print(fun.__annotations__)
print(fun.__doc__)