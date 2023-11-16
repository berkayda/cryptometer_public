import requests
import datetime
from pycryptometer import Cryptometer
c = Cryptometer("YOURAPIKEY")


def merged_orderbook():
    # The best price a buyer is willing to pay for a security is called the “bid,” and the best price the seller is willing to accept is called the “ask.”
    orderbook = c.infos.merged_orderbook()
    print("MERGED ORDERBOOK: ")
    print("Symbol: " + orderbook["symbol"])
    print("Bids: (best price a buyer is willing to pay for a security is called the “bid”)")
    print(orderbook["bids"])
    print("Asks: (best price the seller is willing to accept is called the “ask”)")
    print(orderbook["asks"])
    print("\n")


merged_orderbook()
