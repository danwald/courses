from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class Bid:
    price: Decimal
    quantity: Decimal
    time: datetime


@dataclass
class Ask(Bid):
    pass


class OrderBook:
    def __init__(self, asks=None, bids=None):
        self.asks = asks or []
        self.bids = bids or []
        self.index = 0

    def __iadd__(self, other):
        self.asks.extend(other.asks)
        self.bids.extend(other.bids)
        self.asks = sorted(self.asks, key=lambda x: x.price)
        self.bids = sorted(self.bids, key=lambda x: x.price, reverse=True)
        self.index = 0
        return self

    def __add__(self, other):
        return self.__iadd__(other)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            ask, bid = self.asks[self.index], self.bids[self.index]
        except IndexError:
            self.index = 0
            raise StopIteration
        else:
            self.index += 1
            return ask, bid
