#http://codekata.com/kata/kata09-back-to-the-checkout/
import csv
from pathlib import Path
from collections import Counter
from dataclasses import dataclass
from typing import Any, Protocol
from decimal import Decimal


# https://github.com/faif/python-patterns/blob/master/patterns/behavioral/strategy.py

class Discount(Protocol):
    def get_discounted_price(price: Decimal, quantity: int) -> Decimal: ...

class VolDiscount(Discount):
    quant: int
    price: Decimal

    def __init__(self, quant, price):
        self.quant, self.price = quant, price

    @classmethod
    def parse_discount(cls, record: dict[Any, Any], key='vol', delimiter=':'):
        if st:= record.get(key):
            quant, price = st.split(delimiter)
            return cls(int(quant), Decimal(price))

    def get_discounted_price(self, price: Decimal, quant: int) -> Decimal:
        ret = Decimal(0.0)
        dis_cnt, quant = divmod(quant, self.quant)
        ret += (dis_cnt*self.price)
        ret += quant*price
        return ret

class SaleDiscount(Discount):
    off: Decimal

    def __init__(self, off: Decimal):
        self.off =  off

    @classmethod
    def parse_discount(cls, record: dict[Any, Any], key='sale'):
        if st:= record.get(key):
            return cls(Decimal(st))

    def get_discounted_price(self, price: Decimal, quant: int) -> Decimal:
        return Decimal(quant*Decimal(price)*(Decimal(1.0) - self.off))


class Discounts:
    discounts = (VolDiscount, SaleDiscount)

    @staticmethod
    def get_discount(record: dict[Any, Any]) -> Discount:
        for KlassDiscount in Discounts.discounts:
            if discount:= KlassDiscount.parse_discount(record):
                return  discount
@dataclass
class Item:
    sku: str
    price: Decimal
    discount: Discount | None = None


class Prices(dict):
    @classmethod
    def from_file(cls, path: Path):
        with open(path, newline='') as fp:
            return cls(
                (r['sku'],Item(r['sku'], Decimal(r['cost']), Discounts.get_discount(r)))
                for r in csv.DictReader(fp)
            )

class Checkout(Counter):
    def __init__(self, prices: Prices, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.prices = prices

    @property
    def total(self) -> Decimal:
        ret = Decimal(0.0)
        for sku, quant in self.items():
            price = self.prices[sku]
            if discount:=price.discount:
                ret += discount.get_discounted_price(price.price, quant)
            else:
                ret += quant*price.price
        return ret

    def scan(self, item: str) -> None:
        self.update(item)

def price(items, rules):
    co = Checkout(Prices.from_file(rules))
    co.scan(items)
    return co.total

def test_totals(rules):
    assert 0 == price("", rules)
    assert 50 == price("A", rules)
    assert 80 == price("AB", rules)
    assert 115 == price("CDBA", rules)

    assert 100 == price("AA", rules)
    assert 130 == price("AAA", rules)
    assert 180 == price("AAAA", rules)
    assert 230 == price("AAAAA", rules)
    assert 260 == price("AAAAAA", rules)

    assert 160 == price("AAAB", rules)
    assert 175 == price("AAABB", rules)
    assert 190 == price("AAABBD", rules)
    assert 190 == price("DABABA", rules)
    assert 180 == price("EE", rules)

def test_incremental(rules):
    co = Checkout(Prices.from_file(rules))
    assert   0 == co.total
    co.scan("A");  assert  50 == co.total
    co.scan("B");  assert  80 == co.total
    co.scan("A");  assert 130 == co.total
    co.scan("A");  assert 160 == co.total
    co.scan("B");  assert 175 == co.total


def main():
    rules = 'data/prices.csv'
    test_incremental(rules)
    test_totals(rules)

if __name__ == "__main__":
  main()
