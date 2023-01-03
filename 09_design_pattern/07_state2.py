import abc


class InvalidTransitionError(Exception):
    '''도달 불가능한 상태에서 전이할 때 발생하는 에러'''

class MergeRequestState(abc.ABC): # ABC : 인터페이스 처럼 추상화하는 클래스, 구현 안되면 에러
    def __init__(self, merge_request):
        self._merge_request = merge_request

    @abc.abstractmethod
    def open(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass

    @abc.abstractmethod
    def merge(self):
        pass

    def __str__(self):
        return self.__class__.__name__

class Open(MergeRequestState):
    def open(self):
        self._merge_request.approvals = 0

    def close(self):
        self._merge_request.approvals = 0
        self._merge_request.state = Closed

    def merge(self):
        print(f'{self._merge_request} 머지')
        print(f'{self._merge_request.source_branch} 브랜치 삭제')
        self._merge_request.state = Merged

class Closed(MergeRequestState):
    def open(self):
        print(f"종료된 머지 리퀘스트 {self._merge_request} 재오픈")
        self._merge_request.state = Open

    def close(self):
        pass

    def merge(self):
        raise InvalidTransitionError("종료된 요청을 머지할 수 없음")


class Merged(MergeRequestState):
    def open(self):
        raise InvalidTransitionError("이미 머지 완료됨")

    def close(self):
        raise InvalidTransitionError("이미 머지 완료됨")

    def merge(self):
        pass

class MergeRequst:
    def __init__(self, source_branch: str, target_branch: str) -> None:
        self.source_branch = source_branch
        self.target_branch = target_branch
        self._state : MergeRequestState
        self.approvals = 0
        self.state = Open

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state_cls):
        self._state = new_state_cls(self)

    @property
    def status(self):
        return self._state

    @state.setter
    def state(self, new_state_cls):
        self._state = new_state_cls(self)

    @property
    def status(self):
        return str(self.state)

    def __getattr__(self, method):
        return getattr(self.state, method)

    def __str__(self):
        return f"{self.target_branch}:{self.source_branch}"

if __name__ == '__main__':
    mr = MergeRequst("develop", "master")
    mr.open()
    print("open", mr.approvals)
    mr.approvals = 3
    mr.close()
    print("close", mr.approvals)
    mr.open()
    mr.merge()
    mr.close()