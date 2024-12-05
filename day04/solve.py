type Input = "Map"


class Cursor:
    map: "Map"
    pos: tuple[int, int]
    val: str

    def __init__(self, map: "Map", start_pos: tuple[int, int]) -> None:
        self.map = map
        self.pos = start_pos

    def move_and_get_value(self, relative_pos: tuple[int, int]) -> str | None:
        rx, ry = relative_pos
        new_pos = self.pos[0] + rx, self.pos[1] + ry
        if new_val := self.map.at(new_pos):
            self.pos = new_pos
            self.val = new_val
        return new_val


class Map:
    data: list[str]
    width: int
    height: int

    def __init__(self, lines: list[str]) -> None:
        self.data = lines
        self.width = len(lines[0])
        self.height = len(lines)

    def get_cursor(self, start_pos: tuple[int, int] = (0, 0)):
        return Cursor(self, start_pos)

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
        


def part01(input: Input):
    starting_positions = input.search("X")
    for pos in starting_positions:
        print(pos)


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
