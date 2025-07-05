def main():
    name = input("camelCase: ")
    print("snake_case: ", end="")
    convert_to_snake_case(name)

def convert_to_snake_case(s):
    for i in s:
        if i.isupper():
            print("_", end="")
            print(i.lower(), end="")
        else:
            print(i, end="")
    print("\n")

main()