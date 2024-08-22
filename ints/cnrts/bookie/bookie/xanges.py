from typing import Protocol
from urllib.parse import urljoin
from .data import Ask, Bid


import requests
from datetime import datetime

class Gemini:
    def __init__(self, url='https://api.gemini.com/v1/book/'):
        self.url = url

    def get_book(self, symbol: str) -> dict:
        data = requests.get(urljoin(self.url, symbol)).json()
        return {
            'asks': [
                Ask(ask['price'], ask['amount'], datetime.fromtimestamp(int(ask['timestamp'])))
                for ask in data['asks']
            ],
            'bids': [
                Bid(bid['price'], bid['amount'], datetime.fromtimestamp(int(bid['timestamp'])))
                for bid in data['bids']
            ],
        }
