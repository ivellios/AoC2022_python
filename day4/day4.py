ranged = lambda start, end: range(int(start), int(end) + 1)


def check_contains(range1: str, range2: str):
    range1 = {*ranged(*range1.split("-"))}
    range2 = {*ranged(*range2.split("-"))}

    return range1.issubset(range2) or range2.issubset(range1)


def check_overlaps(range1: str, range2: str):
    range1 = {*ranged(*range1.split("-"))}
    range2 = {*ranged(*range2.split("-"))}

    return bool(range1.intersection(range2))
