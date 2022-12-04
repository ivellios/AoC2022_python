from ..day4_2 import check_duty_overlapping


def test_day4_1():
    input = [
        "2-4,6-8",
        "2-3,4-5",
        "5-7,7-9",
        "2-8,3-7",
        "6-6,4-6",
        "2-6,4-8",
    ]
    total = 0
    for i in input:
        total += check_duty_overlapping(i)

    assert total == 4
