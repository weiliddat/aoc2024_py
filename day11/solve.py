from functools import cache


type Input = list[int]


@cache
def next_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif len(s := str(stone)) % 2 == 0:
        mi = len(s) // 2
        left = int(s[:mi])
        right = int(s[mi:])
        return [left, right]
    else:
        return [stone * 2024]


def part01(input: Input):
    stones = input[:]

    for _ in range(25):
        next_input = []
        for stone in stones:
            next_input += next_stone(stone)
        stones = next_input

    return len(stones)


def part02(input: Input):
    stone_count: dict[int, int] = {}
    for s in input:
        stone_count[s] = stone_count.get(s, 0) + 1

    for _ in range(75):
        next_stone_count: dict[int, int] = {}

        for stone in stone_count:
            count = stone_count[stone]
            for s in next_stone(stone):
                next_stone_count[s] = next_stone_count.get(s, 0) + count

        stone_count = next_stone_count

    return sum(stone_count.values())


def parse_input(input: str) -> Input:
    line = input.splitlines()[0]
    return [int(s) for s in line.split()]


if __name__ == "__main__":
    import os

    dirname = os.path.dirname(__file__)
    input_path = os.path.join(dirname, "input.txt")
    with open(input_path) as input_file:
        input = input_file.read()
        parsed = parse_input(input)
        print(part01(parsed))
        print(part02(parsed))
