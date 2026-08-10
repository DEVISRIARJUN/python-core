def fun2():
    yield 10
    yield 20
    yield 30
f=fun2()
print(f)
print(next(f))
print(next(f))
print(next(f))

