import random
import pyfiglet
import sys

list = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1:
    type = input("Input: ")
    randfont = random.choice(list)
    result = pyfiglet.figlet_format(type, font = randfont)
    print("Output: ", result)

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in list:
    type = input("Input: ")
    result = pyfiglet.figlet_format(type, font = sys.argv[2])
    print("Output: \n", result)

else:
    sys.exit("Invalid usage")