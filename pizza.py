import sys
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

table = []


try:
    with open(sys.argv[1]) as file:
        headers = file.readline().rstrip().split(",")
        for line in file:
            x, y, z = line.rstrip().split(",")
            table.append([x, y, z])

except FileNotFoundError:
    sys.exit("File does not exist")


print(tabulate(table, headers, tablefmt="grid"))