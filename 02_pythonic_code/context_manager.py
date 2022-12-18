filepath = ''


# 오류가 발생하는 경우에도 __exit__ 메소드 (close) 호출된다.
# with open(filepath) as f:
#     pass

# DB backup - context 관리자에서 __exit__ 메서드에서 True를 반환하지 않도록 주의하자. True 반환 시, 오류가 발생해도 호출자에게 전달하지 않는다.
def stop_db():
    print("systemctl stop postgresql.service")


def start_db():
    print("systemctl start postgresql.service")


class DBHandler:
    def __enter__(self):
        stop_db()

    def __exit__(self, exc_type, exc_val, exc_tb):
        start_db()


def db_backup():
    print("pg_dump database")


def main():
    with DBHandler():
        db_backup()


########
import contextlib


# 제너레이터 함수
@contextlib.contextmanager
def db_handler():
    stop_db()  # 데코레이터 적용 시, yield 앞의 모든 것은 __enter__메서드의 일부로 취급된다.
    yield 1  # 1을 반환, 그냥 yield라 쓰면 None 반환
    start_db()  # yield 이후 오는 모든 것들을 __exit__으로 볼 수 있다.


######### mixin
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_db()

    def __exit__(self, exc_type, exc_val, exc_tb):
        start_db()

@dbhandler_decorator()
def offline_backup():
    print('pg_dump database')


if __name__ == '__main__':
    # main()

    # with db_handler() as a:
    #     print(a)
    #     db_backup()

    # with 가 필요없이 자동 실행된다. 좋지만, 컨텍스트 관리자 내부에서 사용하고자 하는 객체를 얻을 수 없다.
    offline_backup()

