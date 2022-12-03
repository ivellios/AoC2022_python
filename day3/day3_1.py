from .day3 import char_to_value, string_to_set


def rucksack_reorganization(rucksack: str):
    left = string_to_set(rucksack[: len(rucksack) // 2])
    right = string_to_set(rucksack[len(rucksack) // 2 :])
    common = left.intersection(right)
    return char_to_value(common.pop())


def rucksacks(filename):
    total = 0
    with open(filename, "r") as f:
        while True:
            data = f.readline().rstrip("\n")
            if not data:
                break
            total += rucksack_reorganization(data)

    print("Total: ", total)
