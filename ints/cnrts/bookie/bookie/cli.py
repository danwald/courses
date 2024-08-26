import argparse
from decimal import Decimal

from bookie import *


def most(amount, include_kraken):
    pass


def no_match(amount, include_kraken):
    bids, asks, bid_cost, ask_cost = (
        Decimal(amount),
        Decimal(amount),
        Decimal(0),
        Decimal(0),
    )
    books = get_books(include_kraken)
    while bids > 0 and asks > 0:
        for ask, bid in books:
            print(f"bid: {bid.price} {bid.quantity} ask: {ask.price} {ask.quantity}")
            if bids > 0:
                bids -= bid.quantity
                bid_cost += bid.price * bid.quantity
                if bids < 0:
                    bid_cost += bid.price * bids
                    bids = 0
            if asks > 0:
                asks -= ask.quantity
                ask_cost += ask.price * ask.quantity
                if asks < 0:
                    ask_cost += ask.price * asks
                    asks = 0
        if bids or asks:
            print("getting more books to finish the trade")
            books += get_books(include_kraken)
            bids, asks = Decimal(amount), Decimal(amount)

    print(f"Total cost of bids: {bid_cost}")
    print(f"Total cost of asks: {ask_cost}")


def get_books(include_kraken):
    books = [xanges.Gemini().get_book(), xanges.Coinbase().get_book()]
    if include_kraken:
        books.append(xanges.Kraken().get_book())
    ob = data.OrderBook()
    for book in books:
        ob += data.OrderBook(asks=book["asks"], bids=book["bids"])
    return ob


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find bids,asks cost USD, for a given amount of BTC"
    )
    parser.add_argument("--amount", help="amount of btc [5.0]", type=float, default=5.0)
    parser.add_argument(
        "--kraken", help="include kraken exchange [False]", action="store_true"
    )
    parser.add_argument(
        "--no-match",
        help="method:no_match - doesnt match, returns max bids/asks in  USD for `amount` of btc; method:match - matches available bids/asks to returns valid trades w.r.t available price. Might be less than `amount`",
        dest="method",
        action="store_const",
        const=no_match,
        default=most,
    )
    args = parser.parse_args()
    args.method(args.amount, args.kraken)
