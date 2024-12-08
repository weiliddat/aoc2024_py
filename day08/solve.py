from functools import reduce
import itertools
from operator import add, attrgetter


type Input = "Map"


class Map:
    data: list[str]
    width: int
    height: int

    def __eq__(self, value) -> bool:
        return (
            self.data == getattr(value, "data")
            and self.width == getattr(value, "width")
            and self.height == getattr(value, "height")
        )

    def __init__(self, lines: list[str]) -> None:
        self.data = lines
        self.width = len(lines[0])
        self.height = len(lines)

    def at(self, pos: tuple[int, int]) -> str | None:
        x, y = pos
        if x < 0 or x >= self.width:
            return None
        if y < 0 or y >= self.height:
            return None
        return self.data[y][x]

    def search(self, v: str):
        for x in range(self.width):
            for y in range(self.height):
                if self.at((x, y)) == v:
                    yield (x, y)

    def frequencies(self):
        return set([char for line in self.data for char in line if char != "."])


def part01(input: Input):
    frequencies = input.frequencies()
    fq_poss = {f: list(input.search(f)) for f in frequencies}
    fq_nodes = {f: set() for f in frequencies}

    for fq in frequencies:
        pairs = itertools.combinations(fq_poss[fq], 2)
        for pair in pairs:
            a = pair[0]
            b = pair[1]
            d = b[0] - a[0], b[1] - a[1]
            a_node = a[0] - d[0], a[1] - d[1]
            if input.at(a_node) is not None:
                fq_nodes[fq].add(a_node)
            b_node = b[0] + d[0], b[1] + d[1]
            if input.at(b_node) is not None:
                fq_nodes[fq].add(b_node)

    uniq_nodes = reduce(lambda a, b: a.union(b), fq_nodes.values())
    return len(uniq_nodes)


def part02(input: Input):
    pass


def parse_input(input: str) -> Input:
    return Map(input.splitlines())


if __name__ == "__main__":
    import os

    dirname = os.path.dirname(__file__)
    input_path = os.path.join(dirname, "input.txt")
    with open(input_path) as input_file:
        input = input_file.read()
        parsed = parse_input(input)
        print(part01(parsed))
        print(part02(parsed))
