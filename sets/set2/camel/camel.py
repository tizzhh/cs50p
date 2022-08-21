a = input("camelCase: ")

for ch in a:
    if not ch.islower():
        print("_", end="")
        print(ch.lower(), end="")
    else:
        print(ch, end="")
print()