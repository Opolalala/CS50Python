from datetime import date, datetime
import sys
import inflect


def main():
    bdate = input("Date of Birth: ")
    thatday = verify_date(bdate)
    sentence = min_to_words(get_min(thatday))
    sentence = sentence[0].upper() + sentence[1:]
    print(sentence, "minutes")


def verify_date(q):
    try:
        date.fromisoformat(q)
        return q
    except ValueError:
        sys.exit("Invalid date")


def get_min(r):
    today = date.today()
    date_format = "%Y-%m-%d"
    date_obj = datetime.strptime(r, date_format)

    date1 = datetime(today.year, today.month, today.day)
    date2 = datetime(date_obj.year, date_obj.month, date_obj.day)
    diff = date1 - date2
    min = diff.days * 1440
    return min


def min_to_words(s):
    p = inflect.engine()
    words = p.number_to_words(s, andword="")
    return words


if __name__ == "__main__":
    main()