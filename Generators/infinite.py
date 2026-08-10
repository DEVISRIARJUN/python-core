def infinite():
    x = 0
    while True:
        yield x
        x = x + 1
l = infinite()
k=infinite()
print(l)
print(next(l))
print(next(l))
print(next(l))
print("for loop")
for i in l:
    if i > 10:
        break 
    print(i,end=" ")
# print()
# for i in k:
#     print(i,end=" ")
#     if i > 5:
#         break