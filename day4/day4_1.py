from .day4 import check_contains


def run(line):
    return check_contains(*line.split(","))
