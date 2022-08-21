import sys

names = []

while True:
    try:
        a = input("Name: ").strip()
        names.append(a)
    except EOFError:
        break
print()
print("Adieu, adieu,", end="")

if len(names) == 1:
    print(f" to {names[0]}")
    sys.exit()
if len(names) == 2:
    print(f" to {names[0]} and {names[1]}")
    sys.exit()

print(f" to {names[0]},", end="")

for name in names[1:len(names) - 1]:
    print(f" {name},", end="")
print(f" and {names[len(names) - 1]}")