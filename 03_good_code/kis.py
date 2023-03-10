# 나쁜 예
class ComplicatedNamespace:
    ACCEPTED_VALUES = ("id_", "user", "location")

    @classmethod
    def init_with_data(cls, **data):
        instance = cls()
        for key, val in data.items():
            if key in cls.ACCEPTED_VALUES:
                setattr(instance, key, val)
        return instance

cn = ComplicatedNamespace.init_with_data(id_=42, user="root", location="127.0.0.1", extra="excluded")
print(cn.id_, cn.user, cn.location)
print(hasattr(cn, "extra"))

# 좋은 예
class Namespace:
    ACCEPTED_VALUES = ("id_", "user", "location")

    def __init__(self, **data):
        accepted_data = {
            k:v for k, v in data.items() if k in self.ACCEPTED_VALUES
        }
        self.__dict__.update(accepted_data)

cn = Namespace(id_=42, user="root", location="127.0.0.1", extra="excluded")
print(cn.id_, cn.user, cn.location)
print(hasattr(cn, "extra"))
