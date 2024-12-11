type Input = list[str]


def part01(input: Input):
    stones = input[:]

    for r in range(25):
        next_input = []
        for stone in stones:
            if stone == "0":
                next_input.append("1")
            elif len(stone) % 2 == 0:
                mi = len(stone) // 2
                left = str(int(stone[:mi]))
                right = str(int(stone[mi:]))
                next_input.append(left)
                next_input.append(right)
            else:
                next_input.append(str(int(stone) * 2024))
        stones = next_input

    return len(stones)


def part02(input: Input):
    pass


def parse_input(input: str) -> Input:
    line = input.splitlines()[0]
    return line.split()


if __name__ == "__main__":
    import os

    dirname = os.path.dirname(__file__)
    input_path = os.path.join(dirname, "input.txt")
    with open(input_path) as input_file:
        input = input_file.read()
        parsed = parse_input(input)
        print(part01(parsed))
        print(part02(parsed))
