# 같은 클래스의 모든 인스턴스가 모든 속성을 복제하는 객체를 만든다
class SharedAllMixin:
    def __init__(self, *args, **kwargs):
        try:
            self.__class__._attributes
        except AttributeError:
            self.__class__._attributes = {}

        self.__dict__ = self.__class__._attributes
        super().__init__(*args, **kwargs)

class BaseFetcher:
    def __init__(self, source):
        self.source = source

class TagFetcher(BaseFetcher):
    def pull(self):
        print(f'{self.source} tag에서 풀')
        return f"Tag = {self.source}"

class BranchFetcher(BaseFetcher):
    def pull(self):
        print(f'{self.source} 브랜치에서 풀')
        return f"Branch = {self.source}"

