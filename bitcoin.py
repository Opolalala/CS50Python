import requests
import sys

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    exit()


try:
    a = float(sys.argv[1])
    o = response.json()
    value = o["bpi"]["USD"]["rate_float"]
    amount = value * a
    print(f"${amount:,.4f}")


except:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    else:
        sys.exit("Command-line argument is not a number")