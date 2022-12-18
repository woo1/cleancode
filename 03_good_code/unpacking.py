USERS = [(i, f"first_name_{i}", f"last_name_{i}") for i in range(1_000)] # 0 - 1000

class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

def bad_users_from_rows(dbrows)->list:
    '''
    db record에서 사용자를 생성하는 파이썬스럽지 않는 잘못된 예
    :param dbrows:
    :return:
    '''
    return [User(row[0], row[1], row[2]) for row in dbrows]

def users_from_rows(dbrows)->list:
    '''
    db record에서 사용자 생성, 가독성 좋은 예
    :param dbrows:
    :return:
    '''
    return [
        User(user_id, first_name, last_name)
        for (user_id, first_name, last_name) in dbrows
    ]

# function(**{"key": "value"})
## function(key="value") 와 동일함

# 반대로 하면 dictionary로 패킹된다.
def function(**kwargs):
    print(kwargs)

function(key="value")

a = function

a(key="hello")