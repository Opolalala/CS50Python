import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    matches = re.search(r"\"https?://(?:www\.)?youtube.com/embed/(\w+)\"", s)
    if matches:
        return("https://youtu.be/" + matches.group(1))


if __name__ == "__main__":
    main()