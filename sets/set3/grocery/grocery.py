groceries = {

}

while True:
    try:
        item = input().upper()
    except EOFError:
        break
    else:
        if item not in groceries:
            groceries[item] = 1
        else:
            groceries[item] += 1

for item in sorted(groceries):
    print(groceries[item], item)