list = []

while True:
    try:
        grocery = input("").upper()
        list.append(grocery)

    except EOFError:
        break

list.sort()

dict = {}

for item in list:
    if item in dict:
        dict[item] +=1
    else:
        dict[item] = 1


for key, value in dict.items():
    print(value, key)