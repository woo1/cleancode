import unittest
from unittest.mock import Mock
from sample1 import WrappedClient

class TestWrappedClient(unittest.TestCase):
    def test_send_converts_types(self):
        wrapped_client = WrappedClient()
        wrapped_client.client = Mock() # 어떤 종류의 타입에도 사용할 수 있는 편리한 객체, 올바르게 호출되는지 확인한다.
        wrapped_client.send("value", 1)
        wrapped_client.client.send.assert_called_with("value", "1")
