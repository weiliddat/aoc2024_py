type Input = list[int]


def part01(input: Input):
    disk_map: list[int | None] = []
    for id, length in enumerate(input):
        disk_map += [id // 2] * length if id % 2 == 0 else [None] * length

    files_from_end = enumerate(disk_map[::-1])
    non_empty = ((i, id) for i, id in files_from_end if id is not None)
    empty_len = disk_map.count(None)
    files_len = len(disk_map) - empty_len

    defragged: list[int] = []

    for i in range(files_len):
        if (id := disk_map[i]) is not None:
            defragged.append(id)
        else:
            to_move = next(non_empty)
            defragged.append(to_move[1])

    return sum([i * id for i, id in enumerate(defragged)])


def part02(input: Input):
    pass


def parse_input(input: str) -> Input:
    return [int(c) for c in input.strip()]


if __name__ == "__main__":
    import os

    dirname = os.path.dirname(__file__)
    input_path = os.path.join(dirname, "input.txt")
    with open(input_path) as input_file:
        input = input_file.read()
        parsed = parse_input(input)
        print(part01(parsed))
        print(part02(parsed))
