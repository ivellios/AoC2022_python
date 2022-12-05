import os
from pprint import pprint


def parse_stacks(stacks_input: list[str]) -> list[list[str]]:
    stacks = []
    extended_line = stacks_input[0] + " "
    number_of_stacks = len(extended_line) // 4
    stacks.extend([[] for i in range(number_of_stacks)])

    for line in stacks_input:
        extended_line = line.strip("\n") + " "
        stacks_line = list(map(''.join, zip(*[iter(extended_line)]*4)))
        stacks_entries = [entry.strip("[] ").strip("[") for entry in stacks_line]

        for stack_no in range(number_of_stacks):
            if stacks_entries[stack_no] != "":
                stacks[stack_no].append(stacks_entries[stack_no])

    for stack in stacks:
        stack.reverse()

    pprint(stacks)

    return stacks


def process_move_cratemover9000(stacks: list[list[str]], line: str):
    amount, move_from, move_to = [int(val) for val in line.split(" ") if val not in ("move", "from", "to")]
    move_from, move_to = (move_from - 1, move_to - 1)

    for move in range(amount):
        stacks[int(move_to)].append(stacks[int(move_from)].pop())


def process_move_cratemover9001(stacks: list[list[str]], line: str):
    amount, move_from, move_to = [int(val) for val in line.split(" ") if val not in ("move", "from", "to")]
    move_from, move_to = (move_from - 1, move_to - 1)

    stacks[int(move_to)].extend(
        stacks[int(move_from)][-amount:]
    )
    stacks[int(move_from)] = stacks[int(move_from)][:-amount]


def check_input_is_move(line: str) -> bool | None:
    """
    True -> Move
    False -> Stack entries end
    None -> Other type [stack, empty line]
    :param line:
    :return:
    """
    if line.startswith("M"):
        return True
    if line.startswith(" 1"):
        return False
    return None


def process_move(filename: str, cranemover: callable):
    with open(filename, "r+") as f:
        stack_lines = []

        # prepare stacks
        while True:
            data = f.readline()
            if not data:
                break

            line = data.rstrip(os.linesep)

            print(line)

            # reading stacks
            if check_input_is_move(line) is None:
                stack_lines.append(line)

            if check_input_is_move(line) is False:
                f.readline() # read the next line (empty one)
                break

        stacks = parse_stacks(stack_lines)

        # perform moves
        while True:
            data = f.readline()
            if not data:
                break

            line = data.rstrip(os.linesep)

            cranemover(stacks, line)

    pprint(stacks)

    print("Result: ", ''.join([stack[-1] for stack in stacks]))
