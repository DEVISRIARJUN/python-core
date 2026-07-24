#Inventory
class Inventory:
    def __init__(self):
        self.l = []
    def __add__(self,any):
        return self.l.append(any)
i1 = Inventory()


# i1.__add__("pencil")
# Inventory.__add__(i1,"pencil")
