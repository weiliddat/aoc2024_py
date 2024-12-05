type Input = list[str]


def part01(input: Input):
    pass


def part02(input: Input):
    pass


def parse_input(input: str) -> Input:
    return input.splitlines()


if __name__ == "__main__":
    import os

    dirname = os.path.dirname(__file__)
    input_path = os.path.join(dirname, "input.txt")
    with open(input_path) as input_file:
        input = input_file.read()
        parsed = parse_input(input)
        print(part01(parsed))
        print(part02(parsed))
