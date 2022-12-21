def stop_db():
    print("systemctl stop postgresql.service")


def start_db():
    print("systemctl start postgresql.service")

class DBHandler:
    def __enter__(self):
        stop_db()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        start_db()

def stream_db_records(db_handler):
    try:
        while True:
            yield db_handler.read_n_records(10)
    except GeneratorExit:
        db_handler.close()

# 제너레이터 호출할 때마다 DB 핸들러에서 얻은 10개 레코드 반환하고, 반복을 끝내고 close 호출하면 연결도 종료된다.
with DBHandler() as db_handler:
    streamer = stream_db_records(db_handler)
    next(streamer)
    next(streamer)
    streamer.close()