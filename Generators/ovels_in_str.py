# write a program to print only ovels in a string

def vowels(n):
    for i in n:
        if i in "aeiou":
            yield i
n = "pythonprogramming"
for i in vowels(n):
    print(i)
