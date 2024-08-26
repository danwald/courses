from datetime import datetime

import pytest

from bookie.data import *


def test_Ask():
    a = Ask(1.0, 2.0, datetime.now())
    assert a.price == 1.0
    assert a.quantity == 2.0
    assert isinstance(a.time, datetime)


def test_Bid():
    b = Bid(1.0, 2.0, datetime.now())
    assert b.price == 1.0
    assert b.quantity == 2.0
    assert isinstance(b.time, datetime)


def test_OrderBook():
    a = Ask(1.0, 2.0, datetime.now())
    b = Bid(1.0, 2.0, datetime.now())
    ob = OrderBook([a], [b])
    assert ob.asks == [a]
    assert ob.bids == [b]
    assert ob.index == 0

    a2 = Ask(2.0, 3.0, datetime.now())
    b2 = Bid(2.0, 3.0, datetime.now())
    ob2 = OrderBook([a2], [b2])
    ob += ob2
    assert ob.asks == [a, a2]
    assert ob.bids == [b2, b]
    assert ob.index == 0

    assert next(ob) == (a, b2)
    assert next(ob) == (a2, b)
    with pytest.raises(StopIteration):
        next(ob)
