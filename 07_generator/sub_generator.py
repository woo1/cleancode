def sequence(name, start, end):
    print(f"{name} 제너레이터 {start}에서 시작")
    yield from range(start, end)
    print(f"{name} 제너레이터 {end}에서 종료")
    return end # stop iteration 시, end return

def main():
    step1 = yield from sequence("first", 0, 5)
    step2 = yield from sequence("second", step1, 10)
    return step1 + step2 # 종료 시 최종 반환값 확인

g = main()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# 마지막 StopIteration에서만 두 합인 15를 반환한다. 5+10
