import argparse
import logging
import sys
from decimal import *

from bookie import *

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))

def most(amount, include_kraken):
    pass


def no_match(amount, include_kraken):
    bids, asks, bid_cost, ask_cost = (
        Decimal(amount),
        Decimal(amount),
        Decimal(0),
        Decimal(0),
    )
    def transact(acc, cost_acc, quant, price):
        if acc > 0:
            acc -= quant
            cost_acc += price * quant
            if acc < 0: # gone over the amount
                cost_acc += price * acc
                acc = 0
        return acc, cost_acc

    books = get_books(include_kraken)
    while bids > 0 and asks > 0:
        for ask, bid in books:
            logger.debug(f"bid: {bid.price} {bid.quantity} ask: {ask.price} {ask.quantity}")
            bids, bid_cost = transact(bids, bid_cost, bid.quantity, bid.price)
            asks, ask_cost = transact(asks, ask_cost, ask.quantity, ask.price)
        if bids or asks:
            logger.warning("Resetting and getting more books to finish the trade ...")
            books += get_books(include_kraken)
            bids, asks = Decimal(amount), Decimal(amount)

    logger.info(f"Cost of no-match asks:{ask_cost:.2f}$, bids:{bid_cost:.2f}$ for {amount}:BTC")


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
        help="method:no_match - doesnt match, returns max bids/asks in  USD for `amount` of btc; method:match - matches available bids/asks to returns valid trades w.r.t available price. Might be less than `amount` as not enough bids or asks available. [match]",
        dest="method",
        action="store_const",
        const=no_match,
        default=most,
    )
    args = parser.parse_args()
    args.method(args.amount, args.kraken)
