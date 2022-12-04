from .day4 import check_contains, check_overlaps


def check_duty_overlapping(line):
    return check_overlaps(*line.split(","))


def duties_overlapping(filename):
    total = 0
    with open(filename, "r") as f:
        while True:
            data = f.readline().rstrip("\n")
            if not data:
                break
            total += check_duty_overlapping(data)

    print("Total: ", total)
