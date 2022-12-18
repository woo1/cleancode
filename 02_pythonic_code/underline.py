class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout = 60

conn = Connector("postgresql://localhost")
print(conn.source, conn._timeout) #_timeout 이런식으로 앞에 _를 붙여주면 자동완성이 안된다. private 권장
