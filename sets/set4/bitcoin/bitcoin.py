import sys, requests, json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    a = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()["bpi"]["USD"]["rate"]
price = float(price.replace(",",""))
price *= a
print(f"${price:,.4f}")