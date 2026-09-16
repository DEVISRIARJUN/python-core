# # Q7. Create:
# • Class Sorter with change(strategy) method. Separate strategy classes: BS, MS, QS,
# each implementing a different logic method.
# Demonstrate how polymorphism can be achieved without inheritance by using
# interchangeable strategy objects.


class BS:
    def logic(self, data):
        print("Using Bubble Sort")
        return sorted(data)
    
class MS:
    def logic(self, data):
        print("Using Merge Sort")
        return sorted(data)

class QS:
    def logic(self, data):
        print("Using Quick Sort")
        return sorted(data)

class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy
    def change(self, strategy):
        self.strategy = strategy
    def sort(self, data):
        return self.strategy.logic(data)
numbers = [5, 2, 8, 1, 3]

# Using Bubble Sort strategy
s = Sorter(BS())
print(s.sort(numbers))

# Changing to Merge Sort strategy
s.change(MS())
print(s.sort(numbers))

# Changing to Quick Sort strategy
s.change(QS())
print(s.sort(numbers))
