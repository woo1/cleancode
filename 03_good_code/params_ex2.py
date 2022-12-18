def show(e, rest):
    print(f"요소: {e} - 나머지: {rest}")

first, *rest = [1, 2, 3, 4, 5]
show(first, rest)

*rest, last = range(6)
show(last, rest)

first, *middle, last = range(6)
print(first)
print(middle)
print(last)

first, last, *empty = (1, 2)
print(first)
print(last)
print(empty)