from urllib.parse import urljoin
from decimal import Decimal
from .data import Ask, Bid
import jwt
from cryptography.hazmat.primitives import serialization
import time
import secrets
from cb import COIN_BASE_CRED

import requests
from datetime import datetime


class Gemini:
    def __init__(self, url="https://api.gemini.com/v1/book/"):
        self.url = url

    def get_book(self, symbol: str = "BTCUSD") -> dict:
        data = requests.get(urljoin(self.url, symbol)).json()
        return {
            "asks": [
                Ask(
                    Decimal(ask["price"]),
                    Decimal(ask["amount"]),
                    datetime.fromtimestamp(int(ask["timestamp"])),
                )
                for ask in data["asks"]
            ],
            "bids": [
                Bid(
                    Decimal(bid["price"]),
                    Decimal(bid["amount"]),
                    datetime.fromtimestamp(int(bid["timestamp"])),
                )
                for bid in data["bids"]
            ],
        }


class Kraken:
    def __init__(self):
        self.url = "https://api.kraken.com/0/public/Depth"

    def get_book(self, symbol: str = "XBTUSD") -> dict:
        data = requests.get(f"{self.url}?pair={symbol}").json()
        return {
            "asks": [
                Ask(
                    Decimal(ask[0]),
                    Decimal(ask[1]),
                    datetime.fromtimestamp(int(ask[2])),
                )
                for ask in data["result"]["XXBTZUSD"]["asks"]
            ],
            "bids": [
                Bid(
                    Decimal(bid[0]),
                    Decimal(bid[1]),
                    datetime.fromtimestamp(int(bid[2])),
                )
                for bid in data["result"]["XXBTZUSD"]["bids"]
            ],
        }


class Coinbase:
    def __init__(self):
        self.url = "https://api.coinbase.com/api/v3/brokerage/product_book"

    @staticmethod
    def build_jwt(
        request_method="GET",
        request_host="api.coinbase.com",
        request_path="/api/v3/brokerage/product_book",
    ):
        uri = f"{request_method} {request_host}{request_path}"
        private_key_bytes = COIN_BASE_CRED["privateKey"].encode("utf-8")
        private_key = serialization.load_pem_private_key(
            private_key_bytes, password=None
        )
        jwt_payload = {
            "sub": COIN_BASE_CRED["name"],
            "iss": "cdp",
            "nbf": int(time.time()),
            "exp": int(time.time()) + 120,
            "uri": uri,
        }
        jwt_token = jwt.encode(
            jwt_payload,
            private_key,
            algorithm="ES256",
            headers={"kid": COIN_BASE_CRED["name"], "nonce": secrets.token_hex()},
        )
        return jwt_token

    def get_book(self, symbol: str = "BTC-USD") -> dict:
        data = requests.get(
            f"{self.url}?product_id={symbol}",
            headers={"Authorization": f"Bearer {self.build_jwt()}"},
        ).json()
        timestamp = datetime.fromisoformat(data["pricebook"]["time"])
        return {
            "asks": [
                Ask(Decimal(ask["price"]), Decimal(ask["size"]), timestamp)
                for ask in data["pricebook"]["asks"]
            ],
            "bids": [
                Bid(Decimal(bid["price"]), Decimal(bid["size"]), timestamp)
                for bid in data["pricebook"]["bids"]
            ],
        }
