class NumberSequence:
    def __init__(self, start=0):
        self.current = start

    def next(self):
        current = self.current
        self.current += 1
        return current

seq = NumberSequence(10)
print(seq.next())
print(seq.next())
print(seq.next())

list(zip(NumberSequence(), "abcdef")) # TypeError: zip argument #1 must support iteration
print(list(zip([1,2,3,6], "abcdef"))) # [(1, 'a'), (2, 'b'), (3, 'c'), (6, 'd')]