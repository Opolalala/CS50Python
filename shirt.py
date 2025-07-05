import sys
import os
from PIL import Image, ImageOps

ex1 = os.path.splitext(sys.argv[1])
ex2 = os.path.splitext(sys.argv[2])
exes = [".jpg", "jpeg", ".png"]

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) == 3 and ex1[1] in exes and ex2[1] in exes:
    if ex1[1] == ex2[1]:
        try:
            im1 = Image.open(sys.argv[1])
            im2 = ImageOps.fit(im1, (600,600))
            shirt = Image.open("shirt.png")
            im2.paste(shirt, shirt)
            im2.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("Invalid")
    else:
        sys.exit("Input and output have different extensions")

else:
    sys.exit("Invalid")