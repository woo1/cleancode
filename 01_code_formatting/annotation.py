class Point:
    place_nm: str
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

def locate(latitude: float, longitude: float)->Point:
    '''지도에서 좌표에 해당하는 객체를 검색한다.'''
    return Point(latitude, longitude)

if __name__ == '__main__':
    # print(Point.__annotations__)
    print(locate.__annotations__)