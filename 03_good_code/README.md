## 개발 지침 약어

### 1. DRY/OAOO
중복을 피하자
- DRY : Do not Repeat Yourself
- OAOO : Once and Only Once

### 2. YAGNI
미래 요구 사항에 맞추는 게 아니라, 현재 요구사항을 잘 해결하기 위한 걸 작성하자.
- YAGNI : You Ain't Gonna Need it

### 3. KIS
최소한의 솔루션, 단순하게 작성하자. 정말 이 기능이 다 필요할까?
- KIS : Keep it Simple

### 4. EAFP/LBYL
EAFP는 일단 코드 돌려보고, 동작 안되면 대응한다는 뜻. 코드 실행하고 발생한 예외를 try except 처리 <br>
LBYL은 돌리기 전에 미리 확인하는 것 
- EAFP : Easier to Ask Forgiveness than Permission, 허락보다는 용서가 쉽다.
- LBYL : Look Before You Leap, 도약하기 전에 살펴라.

LBYL 예시
<pre>
if os.path.exists(filepath):
    with open(filepath) as f:
</pre>

파이썬은 EAFP 방식으로 만들어져서, 이렇게 하는 게 좋다.<br>
LBYL보다 EAFP 원칙이 더 바람직하다.
<pre>
try:
    with open(filepath) as f:
except FileNotFoundError as e:
    logger.error(e)
</pre>
