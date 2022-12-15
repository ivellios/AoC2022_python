# from ..day8_2 import run
#
#
# def test_run():
#     res = run("")
from pprint import pprint

from day8.day8_2 import Processor


def test_process():
    input = [
        "30373",
        "25512",
        "65332",
        "33549",
        "35390",
    ]

    p = Processor()
    p.trees_map = [[int(char) for char in row] for row in input]

    pprint(p.trees_map)

    res = p.process()

    assert res == 8
