import csv
import sys


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

firstnames = []
lastnames = []
houses = []

try:
    with open(sys.argv[1], "r") as readfile:
        reader = csv.DictReader(readfile)
        for row in reader:
            last, first = row["name"].split(",")
            firstnames.append(first.strip())
            lastnames.append(last.strip())
            houses.append(row["house"])
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


with open(sys.argv[2], "w") as writefile:
    writer = csv.DictWriter(writefile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for i in range(len(firstnames)):
        writer.writerow({"first": firstnames[i], "last": lastnames[i], "house": houses[i]})