class DataDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return 42

    def __set__(self, instance, value):
        print(f"{instance}를 {value} 값으로 설정")
        instance.__dict__["descriptor"] = value

class ClientClass:
    descriptor = DataDescriptor()

client = ClientClass()
print(client.descriptor)
client.descriptor = 99
print(client.descriptor)
print(vars(client))
del client.descriptor # error, descriptor에서 delete 메서드 호출하게 되는데, 여기서는 구현하지 않았기 떄문
