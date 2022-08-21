a = input("Expression: ").split(" ")
x = float(a[0])
y = a[1]
z = float(a[2])

if y == "/" and z == 0:
    quit()

match y:
    case "+":
        res = x + z
        print(f"{res:.1f}")
    case "-":
        res = x - z
        print(f"{res:.1f}")
    case "*":
        res = x * z
        print(f"{res:.1f}")
    case "/":
        res = x / z
        print(f"{res:.1f}")