from .solve import Map, parse_input, part01, part02

test_input = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


def test_parse_input():
    expected = Map(
        [
            [8, 9, 0, 1, 0, 1, 2, 3],
            [7, 8, 1, 2, 1, 8, 7, 4],
            [8, 7, 4, 3, 0, 9, 6, 5],
            [9, 6, 5, 4, 9, 8, 7, 4],
            [4, 5, 6, 7, 8, 9, 0, 3],
            [3, 2, 0, 1, 9, 0, 1, 2],
            [0, 1, 3, 2, 9, 8, 0, 1],
            [1, 0, 4, 5, 6, 7, 3, 2],
        ]
    )
    parsed = parse_input(test_input)
    assert parsed == expected


def test_part01():
    expected = 36
    actual = part01(parse_input(test_input))
    assert actual == expected


def test_part02():
    expected = 81
    actual = part02(parse_input(test_input))
    assert actual == expected
