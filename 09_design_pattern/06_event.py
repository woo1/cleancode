#책임 연쇄 패턴
import re

class Event:
    pattern = None

    def __init__(self, next_event=None):
        self.successor = next_event

    def process(self, logline: str):
        if self.can_process(logline):
            return self._process(logline)

        if self.successor is not None:
            return self.successor.process(logline)

    def _process(self, logline: str) -> dict:
        parsed_data = self._parse_data(logline)
        return {
            "type": self.__class__.__name__,
            "id": parsed_data["id"],
            "value": parsed_data["value"]
        }

    @classmethod
    def can_process(cls, logline: str) -> bool:
        return cls.pattern.match(logline) is not None

    @classmethod
    def _parse_data(cls, logline: str) -> dict:
        return cls.pattern.match(logline).groupdict()

class LoginEvent(Event):
    pattern = re.compile(r"(?P<id>\d+):\s+login\s+(?P<value>\S+)")

class LogoutEvent(Event):
    pattern = re.compile(r"(?P<id>\d+):\s+logout\s+(?P<value>\S+)")

if __name__ == '__main__':
    chain = LogoutEvent(LoginEvent())
    print(chain.process("567: login User"))
    print(chain.process("569: logout User1"))
