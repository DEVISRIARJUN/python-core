#to create a contect manager we have two methods it s important for the closeing the file concept

# one type s class


class A:
    def __init__(self,fn):
        self.fn = fn
    def __enter__(self):
        print("Entering the file")
        self.f = open(self.fn,"r")
        return self.f
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("Closing the file")
        self.f.close()
obj = A("test.txt")
with obj as f:
    print(f.read())