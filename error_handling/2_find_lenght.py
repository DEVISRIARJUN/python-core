# find length(obj)


def find_len(obj):
    if isinstance(obj,(str,list,tuple,set)):
        c = 0
        for _ in obj:
            c += 1
        return c
    elif isinstance(obj,dict):
        c = 0
        for i,j in obj.items():
            c += 1
        return c
    else:
        raise TypeError("object must be terable")
print(find_len(1))
