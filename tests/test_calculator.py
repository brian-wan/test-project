import pytest

from addapp.calculator import add, divide, parse_number, subtract


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
    "a, b, expected",
    [
        (5, 2, 3),
        (2, 5, -3),
        (0, 0, 0),
        (2.5, 0.5, 2.0),
        (-3, -4, 1),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),
        (-9, 3, -3.0),
        (5, 2, 2.5),
        (0, 5, 0.0),
        (-6, -3, 2.0),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="zero"):
        divide(5, 0)


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
