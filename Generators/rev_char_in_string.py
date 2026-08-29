#  4. Write a generator that yields characters of a string in reverse order.

def rev(string):
    for i in range(len(string)-1,-1,-1):
        yield string[i]
string = "python"
for i in rev(string):
    print(i)
