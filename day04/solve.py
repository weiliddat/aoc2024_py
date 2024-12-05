type Input = "Map"


class Map:
    data: list[str]
    width: int
    height: int

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

    def get_rows(self):
        return self.data

    def get_columns(self):
        return ["".join(col) for col in zip(*self.data)]
    
    # gonna be lazy cos input is square
    def get_diagonals(self):
        pass


def part01(input: Input):
    print(input.width)
    print(input.height)
    print(input.get_columns())


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
