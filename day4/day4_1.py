from .day4 import check_contains


def check_bad_duties(line):
    return check_contains(*line.split(","))


def duties_containing(filename):
    total = 0
    with open(filename, "r") as f:
        while True:
            data = f.readline().rstrip("\n")
            if not data:
                break
            total += check_bad_duties(data)

    print("Total: ", total)
