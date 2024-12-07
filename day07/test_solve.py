from .solve import Equation, parse_input, part01, part02

test_input = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def test_parse_input():
    expected = [
        Equation(190, [10, 19]),
        Equation(3267, [81, 40, 27]),
        Equation(83, [17, 5]),
        Equation(156, [15, 6]),
        Equation(7290, [6, 8, 6, 15]),
        Equation(161011, [16, 10, 13]),
        Equation(192, [17, 8, 14]),
        Equation(21037, [9, 7, 18, 13]),
        Equation(292, [11, 6, 16, 20]),
    ]
    parsed = parse_input(test_input)
    assert parsed == expected


def test_part01():
    expected = 3749
    actual = part01(parse_input(test_input))
    assert actual == expected


def test_part02():
    expected = None
    actual = part02(parse_input(test_input))
    assert actual == expected
