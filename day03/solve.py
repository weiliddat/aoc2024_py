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
    mul_matcher = re.compile(
        r"(?P<mul>mul)\((?P<a1>\d+),(?P<a2>\d+)\)|(?P<dont>don't)\(\)|(?P<do>do)\(\)"
    )

    instructions = [
        match.groupdict() for line in input for match in mul_matcher.finditer(line)
    ]

    sum = 0
    is_exec = True
    for ins in instructions:
        if is_exec and ins.get("mul"):
            sum += int(ins.get("a1", 0)) * int(ins.get("a2", 0))
        if ins.get("dont"):
            is_exec = False
        if ins.get("do"):
            is_exec = True
    return sum


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
