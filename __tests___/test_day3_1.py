import pytest

from day3_1 import rucksack_reorganization, string_to_set, char_to_value


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
        result += rucksack_reorganization(r)

    assert result == 157


def test_rucksack_reorganization_z():
    val = rucksack_reorganization("RddRcjRvZgZNWNgQQb")
    assert val == ord("Z") - ord("A") + 27  # min 1 + 26 for the small letter prio
