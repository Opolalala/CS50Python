def main():
    t = input("What's the time?")
    value = convert(t)
    if 7<= value <=8:
        print("breakfast time")
    elif 12<= value <=13:
        print("lunch time")
    elif 18<= value <=19:
        print("dinner time")

def convert(time):
    x,y = time.split(":")
    x = float(x)
    y = float(y)
    result = x + (y/60)
    return result

if __name__ == "__main__":
    main()