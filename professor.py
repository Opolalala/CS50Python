import random


def main():
    score = 0
    tre = 0
    level = get_level()
    list1, list2 = generate_integer(level)
    for i in range(10):
        print(list1[i], "+", list2[i], "=", end=" ")
        sum = list1[i] + list2[i]
        usersum = int(input(""))
        if usersum == sum:
            score +=1
        else:
            for _ in range(2):
                print("EEE")
                print(list1[i], "+", list2[i], "=", end=" ")
                usersum = int(input(""))
                if usersum == sum:
                    score += 1
                    break
                else:
                    tre += 1

            if tre == 2:
                print(list1[i], "+", list2[i], "=", sum)

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    listx = []
    listy = []
    start = 10**(level-1)
    stop = (10**level)-1
    for _ in range(10):
        listx.append(random.randint(start, stop))
        listy.append(random.randint(start, stop))
    return listx, listy


if __name__ == "__main__":
    main()