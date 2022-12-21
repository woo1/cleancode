# 이터러블 하지 않은 이터레이터
class SequenceIterator:
    def __init__(self, start=0, step=1):
        self.current = start
        self.step = step

    def __next__(self):
        value = self.current
        self.current += self.step
        return value

si = SequenceIterator(1, 2)
print(next(si))
print(next(si))
print(next(si))
# TypeError: 'SequenceIterator' object is not iterable -- __iter__() 메서드 구현 필요
for _ in SequenceIterator():
    pass