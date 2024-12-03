import re


Input = list[str]


def part01(input: Input):
    mul_matcher = re.compile(r"mul\((\d+),(\d+)\)")
    return sum(
        [
            int(match[0]) * int(match[1])
            for line in input
            for match in mul_matcher.findall(line)
        ]
    )


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
