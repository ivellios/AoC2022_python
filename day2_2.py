import os

from day2_consts import (
    expected_results,
    DRAW, LOSE, WIN,
    DRAW_MAP, LOSE_MAP, WIN_MAP,
    my_choices, RESULTS,
    opponent_choices
)


def result_to_choice(op_choice: str, expected_result: str) -> str:
    if expected_results[expected_result] == DRAW:
        return DRAW_MAP[op_choice]
    if expected_results[expected_result] == LOSE:
        return LOSE_MAP[op_choice]
    if expected_results[expected_result] == WIN:
        return WIN_MAP[op_choice]


def compare(op_choice: str, my_choice: str) -> int:
    return RESULTS[my_choices[my_choice]-1][opponent_choices[op_choice]-1]


def calc_result(op_choice: str, my_choice: str) -> int:
    return compare(op_choice, my_choice) + my_choices[my_choice]


def run():
    sum = 0
    with open("day2.txt", "r+") as f:
        while True:
            data = f.readline()
            if not data:
                break

            data = data.rstrip(os.linesep)
            op_choice, expected_result = data.split(" ")
            my_choice = result_to_choice(op_choice, expected_result)
            res = calc_result(op_choice, my_choice)
            sum += res

    print(f"Sum: {sum}")


if __name__ == "__main__":
    run()