import re


def verify_password(line: str) -> bool:
    parser = re.compile(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)\n$")
    lower, upper, letter, password = map(lambda x: int(x) if x.isdigit() else x, parser.match(line).groups())
    return password.count(letter) in range(lower, upper + 1)


def main() -> None:
    with open("day_02_input.txt", "r") as file:
        answer = sum(verify_password(line) for line in file)
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
