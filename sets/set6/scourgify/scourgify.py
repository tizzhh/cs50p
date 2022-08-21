import sys, csv

input = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not ".csv" in sys.argv[1]:
    sys.exit("Not a csv file")

try:
    with open(sys.argv[1], "r") as file:
        pass
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

with open(sys.argv[1], "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        prevname = row["name"]
        last, first = prevname.split(",")
        first = first.lstrip()
        row = {"first": first, "last": last, "house": row["house"]}
        input.append(row)

with open(sys.argv[2], "w") as file1:
    fieldnames=["first", "last", "house"]
    writer = csv.DictWriter(file1, fieldnames=fieldnames)
    writer.writeheader()
    for row in input:
        writer.writerow(row)
