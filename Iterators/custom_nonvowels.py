#create a custom iterator tha ttakes the whoel sentence and return non - vowels only
class Custom:
    def __init__(self,s):
        self.s=s
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.i < len(self.s):
            self.i+=1
            if self.s[self.i-1] not in "aeiouAEIOU":
                return self.s[self.i-1]
        raise StopIteration
s1=Custom("Arjun")
c=iter(s1)
print(next(c))            
print(next(c))     
print(next(c))     
  