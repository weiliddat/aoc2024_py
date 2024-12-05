import os
from typing import TypedDict


class Input(TypedDict):
    rules: list[tuple[int, int]]
    updates: list[list[int]]


def part01(input: Input):
    input


def part02(input: Input):
    pass


def parse_input(input: str) -> Input:
    s = input.split("\n\n")
    rules: list[tuple[int, int]] = []
    updates: list[list[int]] = []
    for line in s[0].splitlines():
        rule_parts = line.split("|")
        rules.append((int(rule_parts[0]), int(rule_parts[1])))
    for line in s[1].splitlines():
        update_parts = line.split(",")
        updates.append([int(p) for p in update_parts])
    return {"rules": rules, "updates": updates}


if __name__ == "__main__":
    import os

    dirname = os.path.dirname(__file__)
    input_path = os.path.join(dirname, "input.txt")
    with open(input_path) as input_file:
        input = input_file.read()
        parsed = parse_input(input)
        print(part01(parsed))
        print(part02(parsed))
