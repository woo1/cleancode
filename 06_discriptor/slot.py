# 클래스가 기대하는 특정 속성만 정의하고, 다른 것은 제한할 수 있다. - 메모리를 덜 사용한다.
class Coordinate2D:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__} ({self.x}, {self.y})"

coord = Coordinate2D(10, 20)
print(coord)
coord.z = 1 # slots 안하면 attribute 에러 안남
