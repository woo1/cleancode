def generator():
    yield 1
    yield 2
    return 3

val = generator()
print(next(val))
print(next(val))
try:
    next(val)
except StopIteration as e:
    print("returned value", e.value)
