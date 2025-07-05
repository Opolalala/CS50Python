import sys

count = 0


if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")


else:
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if not line.strip().startswith("#") and not line.isspace():
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)