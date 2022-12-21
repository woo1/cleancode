def chain(*iterables):
    for it in iterables:
        for value in it:
            yield value

def chain2(*iterables):
    for it in iterables:
        yield from it

def all_powers(n, pow):
    yield from (n ** i for i in range(pow + 1))

print(list(chain("hello", ["world"], ("tuple", "of", "values"))))
print(list(chain2("hello", ["world"], ("tuple", "of", "values"))))
print(list(chain2([[[1, 0, 0]], [0, 10, 1]])))
print(list(all_powers(2, 10)))