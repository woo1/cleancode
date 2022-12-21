def sequence(start=0):
    while True:
        yield start
        start += 1

seq = sequence(10)
print(next(seq))
print(next(seq))
print(list(zip(sequence(), "abcdef")))
