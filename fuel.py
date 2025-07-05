def main():
    while True:
        try:
            fraction = input("Fraction: ")
            y = convert(fraction)
        except:
            pass
        else:
            break

    z = gauge(y)
    print(z)


def convert(fraction):

    x, y = fraction.split("/")
    if int(y) == 0:
        raise ZeroDivisionError
    elif int(x) > int(y):
        raise ValueError
    return round((int(x) / int(y)) * 100)


def gauge(percentage):

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()