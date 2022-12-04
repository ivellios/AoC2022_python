from .day4 import check_contains


def check_bad_duties(line):
    return check_contains(*line.split(","))
