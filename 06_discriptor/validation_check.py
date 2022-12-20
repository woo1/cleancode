class Validation:
    def __init__(self, valid_func, error_msg: str):
        self.valid_func = valid_func
        self.error_msg = error_msg

    def __call__(self, value):
        if not self.valid_func(value):
            raise ValueError(f"{value!r} {self.error_msg}")

class Field:
    def __init__(self, *validations):
        self._name = None
        self.validations = validations

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def validate(self, value):
        for validation in self.validations:
            validation(value)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self._name] = value

class ClientClass:
    descriptor = Field(
        Validation(lambda x: isinstance(x, (int, float)), "는 숫자가 아님"),
        Validation(lambda x: x >= 0, "는 0보다 작음")
    )

client = ClientClass()
client.descriptor = 42
print(client.descriptor)
# client.descriptor = -42 # error!
# client.descriptor = "asd" # error!