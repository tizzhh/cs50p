a = input("Input: ")
remove = "aeiou"

for ch in a:
    if not ch.lower() in remove:
        print(ch, end="")
print()