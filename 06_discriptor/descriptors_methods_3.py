class ProtectedAttribute:
    def __init__(self, requires_role=None)->None:
        self.permission_required = requires_role
        self._name = None

    def __set_name__(self, owner, name):
        print(f"set name {name}")
        self._name = name

    def __set__(self, user, value):
        if value is None:
            raise ValueError(f"{self._name}를 None으로 설정할 수 없음")
        user.__dict__[self._name] = value # __dict__ : class 객체의 속성 정보를 dict 화 한다.

    def __delete__(self, user):
        if self.permission_required in user.permissions:
            user.__dict__[self._name] = None
        else:
            raise ValueError(
                f"{user!s} 사용자는 {self.permission_required} 권한이 없음"
            )

class User:
    """admin 권한을 가진 사용자만 이메일 주소를 삭제할 수 있음"""
    email = ProtectedAttribute(requires_role="admin") # email 필수값 처리

    def __init__(self, username: str, email: str, permission_list: list = None)->None:
        self.username = username
        self.email = email
        self.permissions = permission_list or []

    def __str__(self):
        return self.username

admin = User("root", "root@d.com", ["admin"])
user = User("user", "user1@d.com", ["email", "helpdesk"])
print(admin.email)
del admin.email
print(admin.email is None)
print(user.email)
# user.email = None # error
del user.email