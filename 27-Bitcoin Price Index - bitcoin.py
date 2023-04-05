import sys
import requests

if len(sys.argv) == 2:
    try:
        bitcoin_quantity = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit()
else:
    print("Missing command-line argument")
    sys.exit()

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
r = r.json()

bitcoin_price = r["bpi"]["USD"]["rate_float"]
total_amount = bitcoin_quantity * bitcoin_price
print(f"${total_amount:,.4f}")
