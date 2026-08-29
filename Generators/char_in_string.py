# 3.	Write a generator that yields each character of a string.

def char(s):
    for i in s:
        yield i
# k = char(["h","e","l","l","o"])
s = "hello"
for i in s:
    print(i)

