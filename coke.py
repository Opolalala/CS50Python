
total = 50
print(f"Amount Due: {total}")

while total != 0:
    i = int(input("Insert Coin: "))
    if i == 25 or i == 10 or i == 5:
        if i <= total:
            total = total - i
            print(f"Amount Due: {total}")
        else:
            total = i - total
            print(f"Change Owed: {total}")
            total = 0
    else:
        print(f"Amount Due: {total}")

print("Change Owed: 0")