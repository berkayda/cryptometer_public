import requests
import datetime
from pycryptometer import Cryptometer
c = Cryptometer("YOURAPIKEY")


def liquidations_BTC():
    liqBTC = c.liquidations.btc()
    print("LIQUIDATIONS (BTC): ")
    print("Longs: " + str(liqBTC["longs"]))
    print("Shorts: " + str(liqBTC["shorts"]))
    print("\n")


liquidations_BTC()
