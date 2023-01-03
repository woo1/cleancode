# static method는 첫번째 인자를 별도로 받지 않는다. classmethod는 class를 받는다.

class Person:
    default = "아빠"

    def __init__(self):
        self.data = self.default

    @classmethod
    def class_person(cls):
        return cls()

    @staticmethod
    def static_person():
        return Person()

class Mom(Person):
    default = "엄마"

print(Mom.class_person().default)
print(Mom.static_person().default)