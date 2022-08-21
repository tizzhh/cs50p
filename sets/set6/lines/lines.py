import sys

count = 0

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not ".py" in sys.argv[1]:
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1], "r") as file:
        pass
except FileNotFoundError:
    sys.exit("File does not exist")

with open(sys.argv[1], "r") as file:
    for line in file:
        if not line.lstrip().startswith("#") and line.strip() != '':
            count += 1

print(count)