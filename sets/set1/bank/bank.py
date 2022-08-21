a = input("Greeting: ").lower()

b = a.split()[0]
b = b.replace(",", "")

if b == "hello":
    print("$0")
elif b[0] == "h":
    print("$20")
else:
    print("$100")