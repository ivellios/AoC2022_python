import pytest

from ..day9_1 import is_head_distancing_from_tail, Processor


def test_process():
    input = [
        "R 4",
        "U 4",
        "L 3",
        "D 1",
        "R 4",
        "D 1",
        "L 5",
        "R 2",
    ]
    p = Processor()
    p.lines = input
    p.process()

    assert p.result == 13

@pytest.mark.parametrize(
    "posH,posT,distance",
    (
        ([0, 1], [0, 1], False),
        ([0, 1], [0, 0], False),
        ([5, 4], [5, 5], False),
        ([5, 4], [6, 4], False),
        ([5, 5], [6, 6], False),
        ([4, 4], [2, 4], True),
        ([3, 3], [2, 2], False),
        ([1, 3], [2, 2], False),
        ([0, 3], [2, 2], True),
        ([0, 0], [1, 2], True),
        ([0, 0], [1, 1], False),
    )
)
def test_is_head_distancing_from_tail(posH, posT, distance):
    assert is_head_distancing_from_tail(posH, posT) == distance

