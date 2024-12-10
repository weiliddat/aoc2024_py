from itertools import repeat


type Input = list[int]


def part01(input: Input):
    disk_map: list[int | None] = []
    for id, length in enumerate(input):
        disk_map += [id // 2] * length if id % 2 == 0 else [None] * length

    files_from_end = enumerate(disk_map[::-1])
    non_empty = ((i, id) for i, id in files_from_end if id is not None)
    empty_len = disk_map.count(None)
    files_len = len(disk_map) - empty_len

    compacted: list[int] = []

    for i in range(files_len):
        if (id := disk_map[i]) is not None:
            compacted.append(id)
        else:
            to_move = next(non_empty)
            compacted.append(to_move[1])

    return sum([i * id for i, id in enumerate(compacted)])


def part02(input: Input):
    disk_map: list[tuple[int | None, int]] = []
    for id, length in enumerate(input):
        disk_map.append((id // 2, length) if id % 2 == 0 else (None, length))

    file_count = len(disk_map)
    for i in range(file_count):
        file_idx = -i - 1
        file = disk_map[file_idx]
        if file[0] is None:
            continue

        for j, candidate in enumerate(disk_map[:file_idx]):
            if candidate[0] is None and candidate[1] >= file[1]:
                disk_map.insert(file_idx, (None, file[1]))
                disk_map.pop(file_idx)
                disk_map.pop(j)
                if candidate[1] > file[1]:
                    disk_map.insert(j, (None, candidate[1] - file[1]))
                disk_map.insert(j, (file[0], file[1]))
                break

    blocks = [item for id, length in disk_map for item in repeat(id, length)]
    return sum([i * id for i, id in enumerate(blocks) if id is not None])


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
