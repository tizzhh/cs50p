res = 0
while True:
    try:
        a = input("Fraction: ").split("/")
        x = int(a[0])
        y = int(a[1])
        while x > y:
            a = input("Fraction: ").split("/")
            x = int(a[0])
            y = int(a[1])
            res = round(x/y*100)
        res = round(x/y*100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break

if res <= 1:
    print("E")
elif res >=99:
    print("F")
else:
    print(f"{res}%")