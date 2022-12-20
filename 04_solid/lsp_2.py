class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict):
        return False

    @staticmethod
    def meets_condition_pre(event_data: dict):
        '''
        인터페이스 계약의 사전조건
        ''event_data'' 파라미터가 적절한 형태인지 유효성 검사
        :param event_data:
        :return:
        '''
        assert isinstance(event_data, dict), f"{event_data!r} is not a dict"
        for moment in ("before", "after"):
            assert moment in event_data, f"{moment} not in {event_data}"
            assert isinstance(event_data[moment], dict)

class UnknownEvent(Event):
    '''데이터만으로 식별 불가한 이벤트'''

class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
                event_data["before"].get("session") == 0
                and event_data["after"].get("session") == 1
        )

class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
                event_data["before"].get("session") == 1
                and event_data["after"].get("session") == 0
        )

# 확장
class TransactionEvent(Event):
    '''시스템에서 발생한 트랜잭션 이벤트'''
    @staticmethod
    def meets_condition(event_data: dict):
        return (
                event_data["after"].get("transaction") is not None
        )

# 사전 조건 먼저 검사
class SystemMonitor:
    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        Event.meets_condition_pre(self.event_data)
        event_cls = next(
            (
                event_cls
                for event_cls in Event.__subclasses__()
                if event_cls.meets_condition(self.event_data)
            ),
            UnknownEvent,
        )
        return event_cls(self.event_data)

l1 = SystemMonitor({"before":{"session": 0}, "after":{"session": 1}})
print(l1.identify_event().__class__.__name__)
l1 = SystemMonitor({"before":{"session": 1}, "after":{"session": 0}})
print(l1.identify_event().__class__.__name__)
l1 = SystemMonitor({"before":{"session": 1}, "after":{"transaction":"1"}})
print(l1.identify_event().__class__.__name__)