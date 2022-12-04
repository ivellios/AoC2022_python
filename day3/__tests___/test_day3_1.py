from ..day3_1 import run


def test_rucksack_reorganization():
    rucksacks = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    result = 0
    for r in rucksacks:
        result += run(r)

    assert result == 157


def test_rucksack_reorganization_z():
    val = run("RddRcjRvZgZNWNgQQb")
    assert val == ord("Z") - ord("A") + 27  # min 1 + 26 for the small letter prio
