from .solve import Map, parse_input, part01, part02

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


def test_part02():
    expected = None
    actual = part02(parse_input(test_input))
    assert actual == expected
