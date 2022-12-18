import os

# 값 대체
config = {"dbport":5432}
# dict - get 메서드의 두번째 파라미터 : 기본값 / 값이 바뀌진 않음
print(config.get("dbhost", "localhost"))
print(config)
print(config.get("dbport"))

# 환경변수
print(os.getenv("DBHOST"))
print(os.getenv("DBPORT", 5432))
print(os.getenv("DBPORT"))