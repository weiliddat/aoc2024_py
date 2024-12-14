from .solve import parse_input, part01, part02

test_input = """\
125 17
"""


def test_parse_input():
    expected = [125, 17]
    parsed = parse_input(test_input)
    assert parsed == expected


def test_part01():
    expected = 55312
    actual = part01(parse_input(test_input))
    assert actual == expected


def test_part02():
    expected = 65601038650482
    actual = part02(parse_input(test_input))
    assert actual == expected
