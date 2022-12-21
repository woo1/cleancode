## 바로 써먹을 수 있을 만한 것들 (업무에 적용해보기)
- 05_decorator/sepearte.py
- 05_decorator/db_driver.py

## 제너레이터 목적 : 메모리 절약

iter : 반복 후 안에 있는 요소 제거, iter(list, 8) -> 8 출력 시 stop iteration <br>
아래처럼도 쓸 수 있음
<pre>
import random
 
def func():
    return random.randint(0, 10)
 
iter_y = iter(func, 8)
while True:
    try:
        print(next(iter_y))
    except:
        raise
</pre>
<pre>
# 전부 한 값으로 초기화
a = b = 3
</pre>

## 제너레이터 표현식
항상 리스트 컴프리헨션 대신 제너레이터 표현식을 사용해서, sum, max, min 같은 이터러블 연산 함수를 사용하자.<br>
그게 훨씬 효율적인 방식이다.
<pre>
print([x**2 for x in range(10)]) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print((x**2 for x in range(10))) # generator object genexpr at 0x7fee69341b50
</pre>

## 나쁜 코드 개선
bad code
<pre>
def process(self):
    for purchase in self.purchases:
        if purchase > 1000.0:
            ...
</pre>
good code - 1000번 넘게 구매한 이력의 처음 10개만 처리하려고 하는 경우 (generator)
<pre>
from itertools import islice
purchases = islice(filter(lambda p: p> 1000.0, purchases), 10)
stats = PurchasesStats(purchases).process()
</pre>