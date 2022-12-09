import pytest

from ..day8 import Processor


def test_process():
    input = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]

    p = Processor(size=5)

    for row in input:
        row_data = [int(char) for char in row]
        p.res_rows.append(p.process_row(row_data))

    res = p.process()

    assert res == 21


def test_process_row():
    data = [
        ("30373", [1, 0, 0, 1, 1]),
        ("25512", [1, 1, 1, 0, 1]),
        ("65332", [1, 1, 0, 1, 1]),
        ("33549", [1, 0, 1, 0, 1]),
        ("35390", [1, 1, 0, 1, 1]),
    ]

    cols = [
        [3, 2, 6, 3, 3],
        [0, 5, 5, 3, 5],
        [3, 5, 3, 5, 3],
        [7, 1, 3, 4, 9],
        [3, 2, 2, 9, 0],
    ]
    p = Processor(size=5)

    for row, res in data:
        row_data = [int(char) for char in row]
        assert p.process_row(row_data) == res

    for i, col in enumerate(p.cols):
        assert col == cols[i]


def test_process_cols():
    cols = [
        ([3, 2, 6, 3, 3], [1, 0, 1, 0, 1]),
        ([0, 5, 5, 3, 5], [1, 1, 0, 0, 1]),
        ([3, 5, 3, 5, 3], [1, 1, 0, 1, 1]),
        ([7, 1, 3, 4, 9], [1, 0, 0, 0, 1]),
        ([3, 2, 2, 9, 0], [1, 0, 0, 1, 1]),
    ]

    p = Processor(size=5)

    for col, res in cols:
        assert p.process_col(col) == res


def test_cols_to_rows():
    cols = [
        [1, 0, 1, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1],
    ]

    expected = (
        (1, 1, 1, 1, 1),
        (0, 1, 1, 0, 0),
        (1, 0, 0, 0, 0),
        (0, 0, 1, 0, 1),
        (1, 1, 1, 1, 1),
    )

    p = Processor(size=5)
    assert p.cols_to_rows(cols) == expected


def test_union():
    rows = [
        [1, 0, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 0, 1, 1],
    ]

    cols = (
        (1, 1, 1, 1, 1),
        (0, 1, 1, 0, 0),
        (1, 0, 0, 0, 0),
        (0, 0, 1, 0, 1),
        (1, 1, 1, 1, 1),
    )

    expected = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
    ]

    p = Processor(size=5)

    assert p.union(rows, cols) == expected


def test_sum_all():
    data = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1],
    ]
    p = Processor(size=5)
    assert p.sum_all(data) == 21
