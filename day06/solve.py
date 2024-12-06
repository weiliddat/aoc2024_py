import os
from time import sleep
from typing import Literal

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


map_wo_guard_cache: dict[str, list[str]] = dict()


def draw_map_with_guard(map: Map, guard_pos: tuple[int, int], guard_dir: "Direction"):
    # remove the old guard ;)
    cache_key = "".join(map.data)
    if cache_key in map_wo_guard_cache:
        map_wo_guard = map_wo_guard_cache[cache_key]
    else:
        map_wo_guard = [line.replace("^", ".") for line in map.data]
        map_wo_guard_cache[cache_key] = map_wo_guard

    for y, line in enumerate(map_wo_guard):
        if guard_pos[1] == y:
            line_with_guard = line[0 : guard_pos[0]]
            match guard_dir:
                case "n":
                    line_with_guard += "^"
                case "e":
                    line_with_guard += ">"
                case "s":
                    line_with_guard += "v"
                case "w":
                    line_with_guard += "<"
            line_with_guard += line[guard_pos[0] + 1 :]
            print(line_with_guard)
        else:
            print(line)

    print(flush=True)
    sleep(0.2)
    os.system("clear")


type Direction = Literal["n", "e", "s", "w"]


def part01(input: Input):
    guard_pos = next(input.search("^"))
    start_pos = guard_pos
    guard_dir: Direction = "n"
    positions = set([guard_pos])

    while True:
        move_pos = (0, 0)
        match guard_dir:
            case "n":
                move_pos = (0, -1)
            case "e":
                move_pos = (1, 0)
            case "s":
                move_pos = (0, 1)
            case "w":
                move_pos = (-1, 0)
        next_pos = (guard_pos[0] + move_pos[0], guard_pos[1] + move_pos[1])

        space = input.at(next_pos)
        if space is None:
            break
        elif next_pos == start_pos and guard_dir == "n":
            break
        elif space == "#":
            match guard_dir:
                case "n":
                    guard_dir = "e"
                case "e":
                    guard_dir = "s"
                case "s":
                    guard_dir = "w"
                case "w":
                    guard_dir = "n"
        else:
            guard_pos = next_pos
            positions.add(guard_pos)

    return len(positions)


def part02(input: Input):
    obstacles: set[tuple[int, int]] = set()
    guard_pos = next(input.search("^"))
    start_pos = guard_pos
    guard_dir: Direction = "n"
    positions = set([guard_pos])

    while True:
        move_pos = (0, 0)
        match guard_dir:
            case "n":
                move_pos = (0, -1)
            case "e":
                move_pos = (1, 0)
            case "s":
                move_pos = (0, 1)
            case "w":
                move_pos = (-1, 0)
        next_pos = (guard_pos[0] + move_pos[0], guard_pos[1] + move_pos[1])

        space = input.at(next_pos)
        if space is None:
            break
        elif next_pos == start_pos and guard_dir == "n":
            break

        if space == "#":
            match guard_dir:
                case "n":
                    guard_dir = "e"
                case "e":
                    guard_dir = "s"
                case "s":
                    guard_dir = "w"
                case "w":
                    guard_dir = "n"
        else:
            if find_loop(input, next_pos):
                obstacles.add(next_pos)
            guard_pos = next_pos
            positions.add(guard_pos)

    return len(obstacles)


def find_loop(map: Map, obs_pos: tuple[int, int]) -> bool:
    guard_pos = next(map.search("^"))
    guard_dir: Direction = "n"
    positions = set([(*guard_pos, guard_dir)])

    while True:
        move_pos = (0, 0)
        match guard_dir:
            case "n":
                move_pos = (0, -1)
            case "e":
                move_pos = (1, 0)
            case "s":
                move_pos = (0, 1)
            case "w":
                move_pos = (-1, 0)
        next_pos = (guard_pos[0] + move_pos[0], guard_pos[1] + move_pos[1])
        space = map.at(next_pos)
        if space is None:
            return False
        elif (*next_pos, guard_dir) in positions:
            return True
        elif next_pos == obs_pos or space == "#":
            match guard_dir:
                case "n":
                    guard_dir = "e"
                case "e":
                    guard_dir = "s"
                case "s":
                    guard_dir = "w"
                case "w":
                    guard_dir = "n"
        else:
            guard_pos = next_pos
            positions.add((*guard_pos, guard_dir))


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
