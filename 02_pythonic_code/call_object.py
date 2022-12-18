# 입력 파라미터와 동일한 값으로 몇 번이나 호출되었는지를 반환하는 객체
from collections import defaultdict

class CallCount:
    def __init__(self):
        self._counts = defaultdict(int)

    def __call__(self, argument):
        self._counts[argument] += 1
        return self._counts[argument]

cc = CallCount()
print(cc(1))
print(cc(2))
print(cc(1))
print(cc(1))
print(cc("something"))
