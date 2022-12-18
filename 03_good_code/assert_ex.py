# assertion : 절대로 일어나지 않아야 하는 상황, 불가능한 조건
# 반드시 프로그램이 중단되기 때문에, 업무 로직에 섞어서는 안된다.

result = condition.holds()
assert result > 0, "에러 {0}".format(result)
