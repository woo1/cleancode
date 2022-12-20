EVENT_REGISTRY = {}

def register_event(event_cls):
    """모듈에서 접근 가능하도록 이벤트 클래스를 레지스트리에 등록"""
    EVENT_REGISTRY[event_cls.__name__] = event_cls
    return event_cls

class Event:
    """기본 이벤트 객체"""

class UserEvent:
    TYPE = "user"

@register_event
class UserLoginEvent(UserEvent):
    """사용자가 시스템에 접근했을 때 발생하는 이벤트"""

@register_event
class UserLogoutEvent(UserEvent):
    """사용자가 시스템에서 나갈 때 발생하는 이벤트"""
