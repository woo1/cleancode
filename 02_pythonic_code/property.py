import re
# 속성 값을 가져오거나, 수정할 때 특별한 로직이 필요한 경우에만 프로퍼티를 사용하자.

EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+[^@]+")

def is_valid_email(eml: str):
    return re.match(EMAIL_FORMAT, eml) is not None

class User:
    def __init__(self, username):
        self.username = username
        self._email = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if not is_valid_email(new_email):
            raise ValueError(f"유효한 메일 주소가 아닙니다.{new_email}")
        self._email = new_email

u1 = User("james")
u1.email = "jsmith@co"