from .solve import parse_input, part01, part02

test_input = """3   4
4   3
2   5
1   3
3   9
3   3
"""


def test_parse_input():
    expected = ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
    parsed = parse_input(test_input)
    print(f"parsed is {parsed}")
    assert parsed == expected


def test_part01():
    expected = 11
    actual = part01(parse_input(test_input))
    assert actual == expected


def test_part02():
    expected = 31
    actual = part02(parse_input(test_input))
    assert actual == expected
