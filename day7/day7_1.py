import os
from pprint import pprint

from .day7 import Processor


def run(filename):
    p = Processor()
    with open(filename, "r+") as f:
        while True:
            data = f.readline()
            if not data:
                break
            line = data.rstrip(os.linesep)
            pprint(line)
            p.process(line)

    p.process_to_root()
    # pprint(p.tree)
    res = p.get_dirs_size_below(100000)
    print("Result: ", res)
    return res


run.no_file_wrapping = True
