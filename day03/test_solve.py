from .solve import parse_input, part01, part02

test_input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""


def test_parse_input():
    expected = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
    parsed = parse_input(test_input)
    assert parsed == expected


def test_part01():
    expected = 161
    actual = part01(parse_input(test_input))
    assert actual == expected


def test_part02():
    expected = 48
    actual = part02(parse_input(test_input))
    assert actual == expected
