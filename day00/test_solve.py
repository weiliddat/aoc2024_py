from .solve import parse_input, part01, part02

test_input = """
"""


def test_parse_input():
    expected = [""]
    parsed = parse_input(test_input)
    assert parsed == expected


def test_part01():
    expected = None
    actual = part01(parse_input(test_input))
    assert actual == expected


def test_part02():
    expected = None
    actual = part02(parse_input(test_input))
    assert actual == expected
