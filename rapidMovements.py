import requests
import datetime
from pycryptometer import Cryptometer
c = Cryptometer("YOURAPIKEY")


def rapid_movements():
    rapidM = c.infos.rapid_movements()  # Pump-Dump #PARSE
    print("RAPID MOVEMENTS: ")
    print()
    for item in rapidM:
        timestamp = item['timestamp']
        dt_object = datetime.datetime.fromisoformat(timestamp[:-1])
        formatted_time = dt_object.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Pair: {item['pair']}")
        print(f"Exchange: {item['exchange']}")
        print(f"Change detected: % {item['change_detected']}")
        print(f"Side: {item['side']}")
        print(formatted_time + " UTC")
        print()


rapid_movements()
