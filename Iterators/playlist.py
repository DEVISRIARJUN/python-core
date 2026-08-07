class Playlist:
    def __init__(self,l):
        self.lst = l
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.lst):
            song = self.lst[self.index]
            self.index += 1
            return song
        else:
            raise StopIteration
p1 = Playlist(["Irumudi","Fear","Sunflower","aayasher"])
p = iter(p1)
print(next(p))
print(next(p))
print(next(p))
print(next(p))
# print(next(p))
# print(next(p))
for i in p1:
    if i is None:
        break
    print(i)
