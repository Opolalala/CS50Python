import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if hours := re.search(r"(1[012]|[1-9]):?([0-5][0-9])? (AM|PM) to (1[012]|[1-9]):?([0-5][0-9])? (AM|PM)" , s):
        hour1, min1, time1, hour2, min2, time2 = hours.groups()

        if min1 == None:
            min1 = int(0)
        if min2 == None:
            min2 = int(0)
        hour1, min1, hour2, min2, = map(int, [hour1, min1, hour2, min2,])

        if hour1 == 12 and time1 == "AM":
            hour1 = 0
        if hour2 == 12 and time2 == "AM":
            hour2 = 0
        if hour1 == 12 and time1 == "PM":
            hour1 = 12
        if hour2 == 12 and time2 == "PM":
            hour2 = 12

        if hour1 != 12 and time1 == "PM":
            hour1 = hour1 + 12
        if hour2 != 12 and time2 == "PM":
            hour2 = hour2 + 12

        if (
                    not 0 <= hour1 <= 23
                    or not 0 <= min1 <= 59
                    or not 0 <= hour2 <= 23
                    or not 0 <= min2 <= 59
                ):
                    raise ValueError("Invalid arguments")

        return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"
    else:
        raise ValueError("Invalid arguments")


if __name__ == "__main__":
    main()