import logging
from functools import wraps

class DBDriver:
    def __init__(self, dbstring):
        self.dbstring = dbstring

    def execute(self, query):
        return f"{self.dbstring} 에서 쿼리 {query} 실행"

def inject_db_driver(function):
    """데이터베이스 dns 문자열을 받아서 DBDriver 인스턴스를 생성하는 데코레이터"""
    @wraps(function)
    def wrapped(dbstring):
        return function(DBDriver(dbstring))
    return wrapped

@inject_db_driver
def run_query(driver):
    return driver.execute("test_function")

print(run_query("test OK"))

##
# class 사용

from functools import wraps
from types import MethodType


class inject_db_driver2:
    '''문자열을 DBDriver 인스턴스로 변환하여 래핑된 함수에 전달한다'''

    def __init__(self, function):
        self.function = function
        wraps(self.function)(self)

    def __call__(self, dbstring):
        return self.function(DBDriver(dbstring))

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.__class__(MethodType(self.function, instance))

@inject_db_driver2
def run_query2(driver):
    return driver.execute("test_function")

print(run_query2("test OK2"))