def my_func():
    '''
    계산을 수행한다.
    :return: 계산값
    '''
    return None


def data_from_response1(response: dict) -> dict:
    if response['status'] != 200:
        raise ValueError
    return {"data": response['payload']}


def data_from_response(response: dict) -> dict:
    '''
    response에 문제가 없다면, response의 payload를 반환한다.

    -response dict의 예제::
    {
        "status": 200, # <int>
        "timestamp": "...." # 현재 시간의 ISO 포맷 문자열
        "payload": { ... } # 반환하려는 dict 데이터
    }

    - 반환 dict 값의 예제::
    {"data": { .. }}

    - 발생 가능한 예외:
    - HTTP status가 200이 아닌 경우 ValueError 발생
    :param response:
    :return:
    '''
    if response['status'] != 200:
        raise ValueError
    return {"data": response['payload']}


if __name__ == '__main__':
    print(my_func.__doc__)
