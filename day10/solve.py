type Input = "Map"


class Map:
    data: list[list[int]]
    width: int
    height: int

    def __eq__(self, value) -> bool:
        return (
            self.data == getattr(value, "data")
            and self.width == getattr(value, "width")
            and self.height == getattr(value, "height")
        )

    def __init__(self, lines: list[list[int]]) -> None:
        self.data = lines
        self.width = len(lines[0])
        self.height = len(lines)

    def at(self, pos: tuple[int, int]) -> int | None:
        x, y = pos
        if x < 0 or x >= self.width:
            return None
        if y < 0 or y >= self.height:
            return None
        return self.data[y][x]

    def around(self, pos: tuple[int, int]):
        x, y = pos
        n = (x, y - 1)
        e = (x + 1, y)
        s = (x, y + 1)
        w = (x - 1, y)
        if (nv := self.at(n)) is not None:
            yield nv, *n
        if (ev := self.at(e)) is not None:
            yield ev, *e
        if (sv := self.at(s)) is not None:
            yield sv, *s
        if (wv := self.at(w)) is not None:
            yield wv, *w

    def search(self, v: int):
        for y in range(self.height):
            for x in range(self.width):
                if self.at((x, y)) == v:
                    yield (x, y)


def part01(input: Input):
    trailheads = input.search(0)

    sum = 0
    for tp in trailheads:
        curr_set = set([(0, tp[0], tp[1])])

        while True:
            next_set = set()
            for p in curr_set:
                for np in input.around((p[1], p[2])):
                    if np[0] == p[0] + 1:
                        next_set.add(np)
            if next_set:
                curr_set = next_set
            else:
                break

        sum += len(curr_set)
    return sum


def part02(input: Input):
    pass


def parse_input(input: str) -> Input:
    return Map([[int(c) for c in line] for line in input.splitlines()])


if __name__ == "__main__":
    import os

    dirname = os.path.dirname(__file__)
    input_path = os.path.join(dirname, "input.txt")
    with open(input_path) as input_file:
        input = input_file.read()
        parsed = parse_input(input)
        print(part01(parsed))
        print(part02(parsed))
