class InternalDataError(Exception):
    '''
    업무 도메인 데이터의 예외
    '''

# 원본 예외를 포함하고, 다른 오류를 발생시켜서 메시지를 변경할 수 있다.
def process(data_dict, record_id):
    try:
        return data_dict[record_id]
    except KeyError as e:
        raise InternalDataError("Record not present") from e

