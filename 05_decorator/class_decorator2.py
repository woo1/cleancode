from functools import wraps

RETRIES_LIMIT = 3

# 특정 예외에 대해 특정 횟수만큼 재시도하는 데코레이터
class ControlledException(Exception):
    """도메인에서 발생하는 일반적인 예외"""

class WithRetry:

    def __init__(self, retries_limit=RETRIES_LIMIT, allowed_exceptions=None):
        self.retries_limit = retries_limit
        self.allowed_exceptions = allowed_exceptions or (ControlledException,)

    def __call__(self, operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None

            for _ in range(self.retries_limit):
                try:
                    return operation(*args, **kwargs)
                except self.allowed_exceptions as e:
                    print("retrying %s due to %s", operation, e)
                    last_raised = e
                raise last_raised

        return wrapped

@WithRetry(retries_limit=5)
def run_with_custom_retries_limit(task):
    return task.operation()
