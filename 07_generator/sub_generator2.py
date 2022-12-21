class CustomException(Exception):
    pass

def sequence(name, start, end):
    value = start
    print(f"{name} 제너레이터 {start}에서 시작")
    while value < end:
        try:
            received = yield value
            print(f"{name} 제너레이터 {received} 값 수신")
            value += 1
        except CustomException as e:
            print(f"{name} 제너레이터 {e} 에러처리")
            received = yield 'OK'
    return end

def main():
    step1 = yield from sequence("first", 0, 5)
    step2 = yield from sequence("second", step1, 10)
    return step1 + step2 # 종료 시 최종 반환값 확인

g = main()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(g.throw(CustomException("처리가능한 예외 던지기")))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(g.throw(CustomException("두번째 제너레이터 예외 던지기")))
# 마지막 StopIteration에서만 두 합인 15를 반환한다. 5+10
