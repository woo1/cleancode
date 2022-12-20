class LoginEventSerializer:
    def __init__(self, event):
        self.event = event

    def serialize(self)->dict:
        return {
            "username": self.event.username,
            "password": "**민감정보 삭제**",
            "ip": self.event.ip,
            "timestamp": self.event.timestamp.strftime("%Y-%m-%d %H:%M"),
        }

class LoginEvent:
    SERIALIZER = LoginEventSerializer

    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

    def serialize(self)->dict:
        return self.SERIALIZER(self).serialize()

# 문제점
# 1. 클래스가 너무 많아진다. 1:1 매핑으로 점점 많아짐
# 2. 유연하지 않다. password를 가진 다른 클래스에서도 이 필드를 숨기려면 또 호출해야 한다.
# 3. 표준화 : serialize는 모든 이벤트 클래스에 있어야 한다.
