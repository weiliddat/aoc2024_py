from .solve import parse_input, part01, part02

test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def test_parse_input():
    expected = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    parsed = parse_input(test_input)
    assert parsed == expected


def test_part01():
    expected = 2
    actual = part01(parse_input(test_input))
    assert actual == expected


def test_part02():
    expected = 4
    actual = part02(parse_input(test_input))
    assert actual == expected
