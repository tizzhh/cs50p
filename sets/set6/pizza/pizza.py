import sys, csv
from tabulate import tabulate

pizzas = []

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not ".csv" in sys.argv[1]:
    sys.exit("Not a csv file")

try:
    with open(sys.argv[1], "r") as file:
        pass
except FileNotFoundError:
    sys.exit("File does not exist")

with open(sys.argv[1], "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        pizzas.append(row)

print(tabulate(pizzas, headers = "keys", tablefmt="grid"))