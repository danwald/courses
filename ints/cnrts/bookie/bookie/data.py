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
