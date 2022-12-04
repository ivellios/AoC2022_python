from .day4 import check_overlaps


def check_duty_overlapping(line):
    return check_overlaps(*line.split(","))
