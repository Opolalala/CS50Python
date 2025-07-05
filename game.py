import random

while True:
    try:
        level = int(input("Level: "))
        num = random.randint(1,level)
        while True:
            try:
                guess = int(input("Guess: "))
                if guess == num:
                    print("Just right!")
                    break
                elif guess > num:
                    print("Too large!")
                    pass
                elif guess < num:
                    print("Too small!")
                    pass
            except ValueError:
                pass
        break

    except ValueError:
        pass