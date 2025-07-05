list = []

while True:
    try:
        name = input("Input: ")
        list.append(name)

    except EOFError:
        print("\n")
        break

print("Adieu, adieu, to", end = " ")

if len(list) > 2:
    for i in list[:-1]:
        print(i, end=", ")
    print("and",list[-1])

else:
    if len(list) == 1:
        print(list[0])
    else:
        print(list[0],"and",list[1])