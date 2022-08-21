a = 50

while a > 0:
    while True:
        print(f"Amount Due: {a}")
        b = int(input("Insert Coin: "))
        if b == 25 or b == 10 or b == 5:
            break
    a -= b
print(f"Change Owed: {-a}")