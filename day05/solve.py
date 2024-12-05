import functools
import os
from typing import TypedDict


class Input(TypedDict):
    rules: list[tuple[int, int]]
    updates: list[list[int]]


def part01(input: Input):
    sum = 0

    page_ranks: dict[int, list[int]] = {}
    for rule in input["rules"]:
        if ranks := page_ranks.get(rule[0]):
            ranks.append(rule[1])
        else:
            page_ranks[rule[0]] = [rule[1]]

    def cmp_rank(a: int, b: int):
        return -1 if b in page_ranks.get(a, []) else +1

    for update in input["updates"]:
        ordered = sorted(update, key=functools.cmp_to_key(cmp_rank))
        if ordered == update:
            mi = len(update) // 2
            sum += update[mi]

    return sum


def part02(input: Input):
    sum = 0

    page_ranks: dict[int, list[int]] = {}
    for rule in input["rules"]:
        if ranks := page_ranks.get(rule[0]):
            ranks.append(rule[1])
        else:
            page_ranks[rule[0]] = [rule[1]]

    def cmp_rank(a: int, b: int):
        return -1 if b in page_ranks.get(a, []) else +1

    for update in input["updates"]:
        ordered = sorted(update, key=functools.cmp_to_key(cmp_rank))
        if ordered != update:
            mi = len(ordered) // 2
            sum += ordered[mi]

    return sum


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
