from day2_1 import calc_result


def test_day2_1():
    sum = 0

    for data in [
        "A Y",
        "B X",
        "C Z"
    ]:
        op_choice, my_choice = data.split(" ")
        res = calc_result(op_choice, my_choice)
        sum += res

    assert sum == 15
