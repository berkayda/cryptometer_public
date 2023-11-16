import requests
import datetime
from pycryptometer import Cryptometer
c = Cryptometer("YOURAPIKEY")


def open_interest():
    print("Exchange for Open Interest: ")
    Exchange = input()
    print("Coin: ")
    coinName = input() + "USDT"
    openInterest = c.infos.open_interest(Exchange, coinName)  # PARSE
    print("OPEN INTEREST: ")
    print(openInterest)
    print("\n")


open_interest()
