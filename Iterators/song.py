l = ["song1","song2","song3","song4"]
it = iter(l)
it2 = l.__iter__()
print(it,it2,sep="\n")
print(next(it))
print(next(it2))
print(it.__next__())
print(it2.__next__())