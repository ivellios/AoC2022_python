from day3 import string_to_set, char_to_value


def find_badge(group: list) -> str:
    return (
        string_to_set(group[0])
        .intersection(string_to_set(group[1]))
        .intersection(string_to_set(group[2]))
        .pop()
    )


def rucksacks():
    total = 0
    with open("day3.txt", "r") as f:
        while True:
            data = [
                f.readline().rstrip("\n"),
                f.readline().rstrip("\n"),
                f.readline().rstrip("\n"),
            ]
            print(data)
            if not data or "" in data:
                break
            total += char_to_value(find_badge(data))

    print("Total: ", total)


if __name__ == "__main__":
    rucksacks()
