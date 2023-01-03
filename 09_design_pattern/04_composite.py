from collections import Iterable
from typing import Union
# https://www.daleseo.com/python-typing/

class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price

class ProductBundle:
    def __init__(self, name, perc_discount, *products: Iterable[Union[Product, "ProductBundle"]])->None:
        self._name = name
        self._perc_discount = perc_discount
        self._products = products

    @property
    def price(self):
        total = sum(p.price for p in self._products)
        return total * (1-self._perc_discount)
