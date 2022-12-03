import pytest

from day3 import string_to_set, char_to_value


def test_string_to_set():
    assert string_to_set("abcdeeee") == set(["a", "b", "c", "d", "e"])


@pytest.mark.parametrize(
    "char, value",
    (
        ("p", 16),
        ("L", 38),
        ("P", 42),
        ("v", 22),
        ("t", 20),
        ("s", 19),
    ),
)
def test_char_to_value(char, value):
    assert char_to_value(char) == value
