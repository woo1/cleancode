from functools import wraps

RETRIES_LIMIT = 3

# 특정 예외에 대해 특정 횟수만큼 재시도하는 데코레이터
class ControlledException(Exception):
    """도메인에서 발생하는 일반적인 예외"""

def with_retry(retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
    allowed_exceptions = allowed_exceptions or ((ControlledException)) # None 일 경우 뒤 값으로 대체

def retry(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        last_raised = None
        for _ in range(retries_limit):
            try:
                return operation(*args, **kwargs)
            except allowed_exceptions as e:
                print("retrying %s due to", operation, e)
                last_raised = e
        raise last_raised

    return wrapped

@with_retry()
def run_operation(task):
    return task.run()

@with_retry(retries_limit=5)
def run_with_custom_retries_limit(task):
    return task.run()

@with_retry(allowed_exceptions=(AttributeError,))
def run_with_custom_exceptions(task):
    return task.run()

@with_retry(retries_limit=4, allowed_exceptions=(ZeroDivisionError, AttributeError,))
def run_with_custom_params(task):
    return task.run()
