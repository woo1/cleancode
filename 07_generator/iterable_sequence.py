class MappedRange:
    '''특정 숫자 범위에 대해 맵으로 변환'''

    def __init__(self, transformation, start, end):
        self._transformation = transformation
        self._wrapped = range(start, end)

    def __getitem__(self, index):
        value = self._wrapped.__getitem__(index)
        result = self._transformation(value)
        print(f"Index: {index}: {result}")
        return result

    def __len__(self):
        return len(self._wrapped)

mr = MappedRange(abs, -10, 5)
print(mr[0])
print(mr[1])
print(mr[-1])
print(list(mr))