from .solve import Map, parse_input, part01, part02

test_input = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


def test_parse_input():
    expected = Map(
        [
            "............",
            "........0...",
            ".....0......",
            ".......0....",
            "....0.......",
            "......A.....",
            "............",
            "............",
            "........A...",
            ".........A..",
            "............",
            "............",
        ]
    )
    parsed = parse_input(test_input)
    assert parsed == expected


def test_map_frequencies():
    expected = {"0", "A"}
    map = parse_input(test_input)
    actual = map.frequencies()
    assert actual == expected


def test_part01():
    expected = 14
    actual = part01(parse_input(test_input))
    assert actual == expected


def test_part02():
    expected = None
    actual = part02(parse_input(test_input))
    assert actual == expected
