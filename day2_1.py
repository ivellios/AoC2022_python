import os

from day2_consts import RESULTS, my_choices, opponent_choices


def compare(op_choice: str, my_choice: str) -> int:
    return RESULTS[my_choices[my_choice] - 1][opponent_choices[op_choice] - 1]


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
            op_choice, my_choice = data.split(" ")
            print(op_choice, my_choice)
            res = calc_result(op_choice, my_choice)
            sum += res
            print(f"Res: {res} | Sum: {sum}")

    print(f"Sum: {sum}")


if __name__ == "__main__":
    run()
