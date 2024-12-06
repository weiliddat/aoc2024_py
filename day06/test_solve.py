import pytest
from .solve import Map, find_loop, parse_input, part01, part02

test_input = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def test_parse_input():
    expected = Map(
        [
            "....#.....",
            ".........#",
            "..........",
            "..#.......",
            ".......#..",
            "..........",
            ".#..^.....",
            "........#.",
            "#.........",
            "......#...",
        ]
    )
    parsed = parse_input(test_input)
    assert parsed.data == expected.data


def test_part01():
    expected = 41
    actual = part01(parse_input(test_input))
    assert actual == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ((3, 6), True),
        ((6, 7), True),
        ((7, 7), True),
        ((1, 8), True),
        ((3, 8), True),
        ((7, 9), True),
        ((2, 6), False),
    ],
)
def test_find_loop(input, expected):
    map = parse_input(test_input)
    assert find_loop(map, input) == expected


def test_part02():
    expected = 6
    actual = part02(parse_input(test_input))
    assert actual == expected
