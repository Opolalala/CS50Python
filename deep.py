answer = input("What's the answer?").strip().lower().replace("-","").replace(" ","")

if answer == "42" or answer == "fortytwo":
    print("Yes")
else:
    print("No")