from .solve import parse_input, part01, part02

test_input = """\
2333133121414131402
"""


def test_parse_input():
    expected = [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2]
    parsed = parse_input(test_input)
    assert parsed == expected


def test_part01():
    expected = 1928
    actual = part01(parse_input(test_input))
    assert actual == expected


def test_part02():
    expected = None
    actual = part02(parse_input(test_input))
    assert actual == expected
