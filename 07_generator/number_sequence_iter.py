class NumberSequence:
    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        current = self.current
        self.current += 1
        return current

    def __iter__(self):
        return self

seq = NumberSequence(10)

print(list(zip(NumberSequence(10), "abcdef"))) # TypeError: zip argument #1 must support iteration
print(next(seq))
print(next(seq))
word = iter("hello")
print(next(word))
print(next(word))
print(next(word))
print(next(word))
print(next(word))
print(next(word, "default value")) # Stop iteration 대신 default 값 사용