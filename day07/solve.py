import itertools
from operator import add, mul
from typing import Callable, NamedTuple, Sequence


type Input = list["Equation"]


class Equation(NamedTuple):
    test_value: int
    numbers: list[int]

    def __hash__(self) -> int:
        return hash((self.test_value, *self.numbers))


def validate_eq(eq: Equation, ops: Sequence[Callable]):
    a = eq.numbers[0]
    for i in range(len(eq.numbers) - 1):
        b = eq.numbers[i + 1]
        op = ops[i]
        a = op(a, b)
    return a == eq.test_value


def find_possible(eq: Equation, ops: Sequence[Callable]):
    op_slots = len(eq.numbers) - 1
    op_combos = itertools.product(*[ops for _ in range(op_slots)])
    for ops in op_combos:
        if validate_eq(eq, ops):
            return True


def part01(input: Input):
    possible = set()
    operators = [add, mul]

    for eq in input:
        if find_possible(eq, operators):
            possible.add(eq)

    return sum([p.test_value for p in possible])


def part02(input: Input):
    possible = set()
    operators = [add, mul, lambda a, b: int(str(a) + str(b))]

    for eq in input:
        if find_possible(eq, operators):
            possible.add(eq)

    return sum([p.test_value for p in possible])


def parse_input(input: str) -> Input:
    equations = []
    for line in input.splitlines():
        a, b = line.split(":")
        equations.append(Equation(int(a), [int(n) for n in b.split()]))
    return equations


if __name__ == "__main__":
    import os

    dirname = os.path.dirname(__file__)
    input_path = os.path.join(dirname, "input.txt")
    with open(input_path) as input_file:
        input = input_file.read()
        parsed = parse_input(input)
        print(part01(parsed))
        print(part02(parsed))
