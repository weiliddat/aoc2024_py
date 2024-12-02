Input = list[list[int]]


def part01(input: Input):
    return sum([1 for report in input if report_safety(report)])


def report_safety(report: list[int]) -> bool:
    is_asc = None

    for i in range(1, len(report)):
        a = report[i - 1]
        b = report[i]

        if a == b:
            return False
        if abs(a - b) > 3:
            return False

        if is_asc is True and b < a:
            return False
        elif is_asc is False and a < b:
            return False
        elif is_asc is None:
            is_asc = b > a

    return True


def with_problem_dampener(report: list[int]) -> bool:
    for i in range(len(report)):
        rc = report.copy()
        rc.pop(i)
        if report_safety(rc):
            return True
    return False


def part02(input: Input):
    return sum([1 for report in input if with_problem_dampener(report)])


def parse_input(input: str) -> Input:
    return [[int(i) for i in line.split()] for line in input.splitlines()]


if __name__ == "__main__":
    import os

    dirname = os.path.dirname(__file__)
    input_path = os.path.join(dirname, "input.txt")
    with open(input_path) as input_file:
        input = input_file.read()
        parsed = parse_input(input)
        print(part01(parsed))
        print(part02(parsed))
