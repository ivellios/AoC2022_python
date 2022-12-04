import os

from .day2_consts import RESULTS, my_choices, opponent_choices


def compare(op_choice: str, my_choice: str) -> int:
    return RESULTS[my_choices[my_choice] - 1][opponent_choices[op_choice] - 1]


def calc_result(op_choice: str, my_choice: str) -> int:
    return compare(op_choice, my_choice) + my_choices[my_choice]


def choice_result_value(data):
    return calc_result(*data.split(" "))
