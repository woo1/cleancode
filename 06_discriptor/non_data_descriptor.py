class NonDataDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return 42

class ClientClass:
    descriptor = NonDataDescriptor()

client = ClientClass()
print(client.descriptor)
client.descriptor = 49
print(client.descriptor)
del client.descriptor
print(client.descriptor)