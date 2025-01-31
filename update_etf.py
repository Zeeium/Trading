
import json
import random

etfs = {
    "FAKE1": 100.0,
    "FAKE2": 50.0,
    "FAKE3": 75.0,
    "FAKE4": 120.0
}


def update_prices():
    for etf in etfs:
        etfs[etf] += random.uniform(-2, 2)  

   
    with open("etf_data.json", "w") as f:
        json.dump(etfs, f, indent=4)

    print("Updated ETF prices and saved to etf_data.json.")

update_prices()
