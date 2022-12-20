from functools import wraps

# 특정 예외에 대해 특정 횟수만큼 재시도하는 데코레이터
class ControlledException(Exception):
    """도메인에서 발생하는 일반적인 예외"""

def retry(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        last_raised = None
        RETRIES_LIMIT = 3
        for _ in range(RETRIES_LIMIT):
            try:
                return operation(*args, **kwargs)
            except ControlledException as e:
                print("retrying %s", operation.__qualname__)
                last_raised = e
        raise last_raised
    return wrapped

# 이렇게 하면, run_operation = retry(run_operation) 한 걸로 된다.
@retry
def run_operation(task):
    '''실행 중 예외가 발생할 것으로 예상되는 특정 작업 실행'''
    return task.run()
