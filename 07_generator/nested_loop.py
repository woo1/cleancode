# 중첩 루프
import time
# 1. bad code
def search_nested_bad(array, desired_value):
    coords = None
    for i, row in enumerate(array):
        for j, cell in enumerate(row):
            if cell == desired_value:
                coords = (i, j)
                break

        if coords is not None:
            break

    if coords is None:
        raise ValueError(f"{desired_value} not found")

    print(f"{coords}에서 값 {desired_value} 찾음")
    return coords

# 2. good code - 속도는 더 느림
def _iterate_array2d(array2d):
    for i, row in enumerate(array2d):
        for j, cell in enumerate(row):
            yield (i, j), cell

def search_nested(array, desired_value):
    try:
        coords = next(
            coord
            for (coord, cell) in _iterate_array2d(array)
            if cell == desired_value
        )
    except StopIteration:
        raise ValueError(f"{desired_value} not found")

    print(f"{coords}에서 값 {desired_value} 찾음")
    return coords

stt = time.time()
print(search_nested([[1, 2, 3, 4, 5, 101], [120, 11, 33]], 120))
print(time.time() - stt)

stt = time.time()
print(search_nested_bad([[1, 2, 3, 4, 5, 101], [120, 11, 33]], 120))
print(time.time() - stt)