from functools import wraps

# 함수 실행 시 로그 남기는 데코레이터
def trace_decorator(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        print(f"{function.__qualname__} 실행") # A.AA.f
        return function(*args, **kwargs)

    return wrapped

@trace_decorator
def process_account(account_id):
    '''ID별 계정 처리'''
    print(f"{account_id} 계정처리")

process_account("user1")
print(process_account.__qualname__)

## 일반적인 구조
def decorator(original_func):
    @wraps(original_func)
    def decorated_func(*args, **kwargs):
        # 데코레이터에 의한 수정 작업
        return original_func(*args, **kwargs)

    return decorated_func
