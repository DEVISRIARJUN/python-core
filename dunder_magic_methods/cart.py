class Cart:
    def __init__(self):
        self.l = []
    def __add__(self,items):
        if items not in self.l:
            self.l.append(items)
        return self
    def __sub__(self,items):
        if items in self.l:
            self.l.remove(items)
        return self
    def __str__(self):
        return f"Cart items:{self.l}"
c1 = Cart()
c1+"chips"+"Milkshake"+"Thumpsup"+"Tomato"
c1-"Laptop"-"chips"-"mobile"-"Tomato"
print(c1)
