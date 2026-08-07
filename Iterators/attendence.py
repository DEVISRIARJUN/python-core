class Attendence:
    def __init__(self,st):
        self.students = st
        self.roll_no = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.roll_no < len(self.students):
            name = self.students[self.roll_no]
            self.roll_no += 1
            return name
        else:
            raise StopIteration
st1 = Attendence(["seenu","shiva","lokesh","gunneshwarao","prmaila","rekha"])
st2 = Attendence(["raj","nikhil","gunasekhar","agamba"])
for i in st1:
    print(f"{i} : present")
for i in st2:
    print(f"{i} : present")