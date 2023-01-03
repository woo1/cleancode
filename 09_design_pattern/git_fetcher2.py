# 생성 패턴 - 객체 인스턴스화할 때의 복잡성을 최대한 추상화, 단순화
from shared import SharedAttribute
# 동일한 로직을 현재 태그 기준이 아니라, 현재 브랜치 기준으로 적용하고 싶은 경우 -> 클래스 속성만 추가하면 된다.
class GitFetcher:
    current_tag = SharedAttribute()
    current_branch = SharedAttribute()

    def __init__(self, tag, branch=None):
        self.current_tag = tag
        self.current_branch = branch

    def pull(self):
        print(f'{self.current_branch} {self.current_tag}에서 풀')
        return self.current_tag

if __name__ == '__main__':
    f1 = GitFetcher(0.1, 'main')
    f2 = GitFetcher(0.2, 'main')
    f1.current_branch = 'develop'
    f1.current_tag = 0.3
    f2.pull() # 0.3
    f1.pull() # 0.3