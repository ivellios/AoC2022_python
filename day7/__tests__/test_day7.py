import json

import pytest

from day7.day7 import Processor


def test_parse_dirs():
    input = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]

    p = Processor()
    for line in input:
        p.process(line)
    p.process_to_root()

    result = p.tree
    assert json.dumps(result) == json.dumps({'["/"]': 48381165, '["/", "a"]': 94853, '["/", "a", "e"]': 584, '["/", "d"]': 24933642})

def test_get_dir():
    p = Processor()
    p.tree = {'["/"]': 48381165, '["/", "a"]': 94853, '["/", "a", "e"]': 584, '["/", "d"]': 24933642}

    result = p.get_dirs_size_below(100000)

    assert result == 95437
