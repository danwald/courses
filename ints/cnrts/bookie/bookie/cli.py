from bookie import *
from decimal import Decimal


def no_match(*args, **kwargs):
    amount = 5
    include_kraken = True
    bids, asks, bid_cost, ask_cost = Decimal(amount), Decimal(amount), Decimal(0), Decimal(0)
    books = get_books(include_kraken)
    while bids > 0 and asks > 0:
        for ask, bid in books:
            print (f"bid: {bid.price} {bid.quantity} ask: {ask.price} {ask.quantity}")
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
            print('getting more books to finish the trade')
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
        ob += data.OrderBook(asks=book['asks'], bids=book['bids'])
    return ob



if __name__ == '__main__':
    no_match()
