# 데코레이터, 관신사 분리
# 나쁜 예
from functools import wraps
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# log 출력 형식
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# log를 파일에 출력
file_handler = logging.FileHandler('my.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def traced_function(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        logger.info("%s 함수 실행", function.__qualname__)
        start_time = time.time()
        result = function(*args, **kwargs)
        logger.info("함수 %s 처리 소요시간 %.2fs",
                    function.__qualname__,
                    time.time(), - start_time)
        return result
    return wrapped

# 좋은 예
def log_execution(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        logger.info("started execution of %s", function.__qualname__)
        return function(*args, **kwargs)
    return wrapped

def measure_time(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)

        logger.info("function %s took %.2f", function.__qualname__, time.time()-start_time)
        return result
    return wrapped

@measure_time
@log_execution
def operation():
    time.sleep(2)

operation()