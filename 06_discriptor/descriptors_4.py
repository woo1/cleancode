class DescriptorWithName:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, owner, name):
        self.name = name

class ClientClass:
    descriptor = DescriptorWithName()
