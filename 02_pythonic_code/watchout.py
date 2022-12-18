
# 1. 변경 가능한(mutable) 값을 파라미터 기본값으로 쓰지 않는다.
# 1번 호출 후 기본값이 사라지기 때문
def wrong_user_display(user_metadata = {"name":"Jhon", "age":30}):
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} {age}"

def user_display(user_metadata=None):
    if user_metadata is None:
        user_metadata = {"name": "Jhon", "age": 30}
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} {age}"

print(wrong_user_display())
print(wrong_user_display({"name":"James", "age":26}))
# print(wrong_user_display()) # error!

print(user_display())
print(user_display({"name":"James", "age":26}))
print(user_display()) # error!