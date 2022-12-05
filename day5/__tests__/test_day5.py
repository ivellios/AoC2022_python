from ..day5 import parse_stacks, process_move_cratemover9000, process_move_cratemover9001


def test_parse_stacks():
    stacks_input = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
    ]
    stacks = parse_stacks(stacks_input)

    assert stacks == [
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"]
    ]


def test_parse_moves_cratemover9000():
    moves = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

    stacks = [
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"]
    ]

    for line in moves:
        process_move_cratemover9000(stacks, line)

    assert stacks == [
        ["C"],
        ["M"],
        ["P", "D", "N", "Z"]
    ]


def test_parse_moves_cratemover9001():
    moves = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2",
    ]

    stacks = [
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"]
    ]

    for line in moves:
        process_move_cratemover9001(stacks, line)

    assert stacks == [
        ["M"],
        ["C"],
        ["P", "Z", "N", "D"]
    ]
