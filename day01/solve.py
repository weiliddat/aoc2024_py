Input = tuple[list[int], list[int]]


def part01(input: Input):
    first = input[0].copy()
    second = input[1].copy()
    first.sort()
    second.sort()
    distances = [abs(pairs[0] - pairs[1]) for pairs in zip(first, second)]
    return sum(distances)


def part02(input: Input):
    first = input[0].copy()
    second = input[1].copy()
    similarities = [i * second.count(i) for i in first]
    return sum(similarities)


def parse_input(input: str) -> Input:
    first_list = []
    second_list = []
    for line in input.splitlines():
        row_strs = line.split()
        first_list.append(int(row_strs[0]))
        second_list.append(int(row_strs[1]))
    return (first_list, second_list)


if __name__ == "__main__":
    import os

    dirname = os.path.dirname(__file__)
    input_path = os.path.join(dirname, "input.txt")
    with open(input_path) as input_file:
        input = input_file.read()
        parsed = parse_input(input)
        print(part01(parsed))
        print(part02(parsed))
