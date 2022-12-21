print([x**2 for x in range(10)]) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print((x**2 for x in range(10))) # <generator object <genexpr> at 0x7fee69341b50>
print(sum(x**2 for x in range(10))) # 285, 이터러블 연산 가능한 함수에 list처럼 직접 전달 가능
