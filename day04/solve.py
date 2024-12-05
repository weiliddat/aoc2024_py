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
        if x < -self.width or x >= self.width:
            return None
        if y < -self.height or y >= self.height:
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
        diagonals: list[str] = []

        for i in range(self.width):
            diagonal = []
            for j in range(i + 1):
                x = i - j
                y = j
                diagonal.append(self.at((x, y)))
            diagonals.append("".join(diagonal))

        for i in range(self.width - 1):
            diagonal = []
            for j in range(i + 1):
                x = -(i - j) - 1
                y = -j - 1
                diagonal.append(self.at((x, y)))
            diagonals.append("".join(diagonal))

        for i in range(self.width):
            diagonal = []
            for j in range(i + 1):
                x = -(i - j) - 1
                y = j
                diagonal.append(self.at((x, y)))
            diagonals.append("".join(diagonal))

        for i in range(self.width - 1):
            diagonal = []
            for j in range(i + 1):
                x = i - j
                y = -j - 1
                diagonal.append(self.at((x, y)))
            diagonals.append("".join(diagonal))

        return diagonals


def part01(input: Input):
    xmas_count = 0
    lines = [
        *input.get_rows(),
        *input.get_columns(),
        *input.get_diagonals(),
    ]
    for line in lines:
        xmas_count += line.count("XMAS")
        xmas_count += line.count("SAMX")
    return xmas_count


def part02(input: Input):
    xmas_count = 0
    start_poss = input.search("A")
    for a in start_poss:
        # ignore first/last line/cols
        if (
            a[0] == 0
            or a[0] == input.width - 1
            or a[1] == 0
            or a[1] == input.height - 1
        ):
            continue

        if (
            (
                input.at((a[0] - 1, a[1] - 1)) == "M"
                and input.at((a[0] + 1, a[1] + 1)) == "S"
            )
            or (
                input.at((a[0] - 1, a[1] - 1)) == "S"
                and input.at((a[0] + 1, a[1] + 1)) == "M"
            )
        ) and (
            (
                input.at((a[0] + 1, a[1] - 1)) == "M"
                and input.at((a[0] - 1, a[1] + 1)) == "S"
            )
            or (
                input.at((a[0] + 1, a[1] - 1)) == "S"
                and input.at((a[0] - 1, a[1] + 1)) == "M"
            )
        ):
            xmas_count += 1

    return xmas_count


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
