import requests
import datetime
from pycryptometer import Cryptometer
c = Cryptometer("YOURAPIKEY")


def liquidations_BitmexXBTUSD():
    # Shows for only "XBTUSD" parity
    liqBitmex = c.liquidations.bitmex("XBTUSD")  # PARSE
    print("LIQUIDATIONS Bitmex: ")
    print()
    for item in liqBitmex:
        timestamp = item['timestamp']
        dt_object = datetime.datetime.fromisoformat(timestamp[:-1])
        formatted_time = dt_object.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Market Pair: {item['market_pair']}")
        print(f"Quantity: {item['quantity']}")
        print(f"Side: {item['side']}")
        print(formatted_time + " UTC")
        print("\n")


liquidations_BitmexXBTUSD()
