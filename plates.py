def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if is_num(s[:2]) and is_alphanum(s) and is_len(s) and first_num(s):
        return True
    else:
        return False


def first_num(l):
    for i in l:
        if i.numeric():
            if i == 0:
                return False

def is_num(m):
    for i in m:
        if not i.isdigit():
            return False
    return True


def is_len(n):
    if 2 <= len(n) <= 6:
        return True
    else:
        return False


def is_alphanum(o):
    for i in o:
        if not i.isdigit() and not i.isalpha():
            return False
    return True


main()