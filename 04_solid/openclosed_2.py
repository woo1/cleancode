# 추상화 예시
class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict):
        return False

class UnknownEvent(Event):
    '''데이터만으로 식별 불가한 이벤트'''

class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
                event_data["before"]["session"] == 0
                and event_data["after"]["session"] == 1
        )

class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
                event_data["before"]["session"] == 1
                and event_data["after"]["session"] == 0
        )

class SystemMonitor:
    '''시스템에서 발생한 이벤트 분류'''

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            print('1', event_cls)
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)

l1 = SystemMonitor({"before":{"session": 0}, "after":{"session": 1}})
print(l1.identify_event().__class__.__name__)
l1 = SystemMonitor({"before":{"session": 1}, "after":{"session": 0}})
print(l1.identify_event().__class__.__name__)
l1 = SystemMonitor({"before":{"session": 1}, "after":{"session": 1}})
print(l1.identify_event().__class__.__name__)