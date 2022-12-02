from day2_2 import result_to_choice, calc_result


def test_day2_2():
    sum = 0

    for data in [
        "A Y",
        "B X",
        "C Z",
    ]:
        op_choice, expected_result = data.split(" ")
        my_choice = result_to_choice(op_choice, expected_result)
        res = calc_result(op_choice, my_choice)
        sum += res

    assert sum == 12
