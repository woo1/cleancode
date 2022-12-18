
def function(arg):
    arg += " in function" # 최대한 이런, 파라미터 변경을 안하는 게 좋다.
    print(arg)

# call by value
immutable = "hello"
function(immutable)
print(immutable)

# call by reference
mutable = list("hello")
function(mutable)
print(mutable)

