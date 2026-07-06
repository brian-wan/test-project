import pytest

from addapp.calculator import add, parse_number


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (0, 0, 0),
        (2.5, 0.5, 3.0),
        (-3, -4, -7),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("3", 3.0),
        ("-2.5", -2.5),
        ("  4  ", 4.0),
        ("0", 0.0),
    ],
)
def test_parse_number_valid(text, expected):
    assert parse_number(text) == expected


@pytest.mark.parametrize("text", ["abc", "", "1,2", "1+2"])
def test_parse_number_invalid_raises(text):
    with pytest.raises(ValueError):
        parse_number(text)
