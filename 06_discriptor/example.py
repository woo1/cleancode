class Traveller:
    def __init__(self, name, current_city):
        self.name = name
        self._current_city = current_city
        self._cities_visited = [current_city]

    @property
    def current_city(self):
        return self._current_city

    @current_city.setter
    def current_city(self, new_city):
        if new_city != self._current_city:
            self._cities_visited.append(new_city)
            self._current_city = new_city

    @property
    def cities_visited(self):
        return self._cities_visited

alice = Traveller("Alice", "Barcelona")
alice.current_city = "Paris"
alice.current_city = "Seoul"
alice.current_city = "Tokyo"
alice.current_city = "Jeju"
print(alice.cities_visited)

# 방문 국가, 티켓 추적하려면 추가 구현 필요 -> 디스크립터 사용 -> example_desc.py
