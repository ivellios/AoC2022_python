from .day3 import char_to_value, string_to_set


def run(rucksack: str):
    left = string_to_set(rucksack[: len(rucksack) // 2])
    right = string_to_set(rucksack[len(rucksack) // 2 :])
    common = left.intersection(right)
    return char_to_value(common.pop())
