import pytest

from ..day4 import check_contains, check_overlaps


@pytest.mark.parametrize(
    "range1,range2,result",
    (
        ("2-4", "6-8", False),
        ("2-3", "4-5", False),
        ("5-7", "7-9", False),
        ("2-8", "3-7", True),
        ("6-6", "4-6", True),
        ("2-6", "4-8", False),
    ),
)
def test_check_contains(range1, range2, result):
    assert check_contains(range1, range2) == result


@pytest.mark.parametrize(
    "range1,range2,result",
    (
        ("2-4", "6-8", False),
        ("2-3", "4-5", False),
        ("5-7", "7-9", True),
        ("2-8", "3-7", True),
        ("6-6", "4-6", True),
        ("2-6", "4-8", True),
    ),
)
def test_check_overlaps(range1, range2, result):
    assert check_overlaps(range1, range2) == result
