from collections import UserList

# list는 정확히 __getitem__ 호출 되지 않기 때문에, UserList 사용
# dict -> collections.UserDict
# list -> collections.UserList
# str -> collections.UserString
class GoodList(UserList):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        if index % 2 == 0:
            prefix = "짝수"
        else:
            prefix = "홀수"
        return f"[{prefix}] {value}"

gl = GoodList((0, 1, 2))
print(gl[0])
print(gl[1])
print(';'.join(gl))