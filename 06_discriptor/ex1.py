import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# log 출력 형식
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# log를 파일에 출력
file_handler = logging.FileHandler('my.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Attribute:
    value = 42

class Client:
    attribute = Attribute()

print(Client().attribute)
print(Client().attribute.value)

class DescriptorClass:
    def __get__(self, instance, owner): # instance : 디스크립터를 호출한 객체(client), owner: 해당 객체의 클래스, ClientClass
        if instance is None:
            return self
        logger.info("Call: %s.__get__(%r, %r)", self.__class__.__name__, instance, owner)
        return instance

class ClientClass:
    descriptor = DescriptorClass()

client = ClientClass()
print(client.descriptor)
print(client.descriptor is client)
