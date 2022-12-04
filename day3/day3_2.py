from .day3 import string_to_set, char_to_value


def find_badge(group: list) -> str:
    return (
        string_to_set(group[0])
        .intersection(string_to_set(group[1]))
        .intersection(string_to_set(group[2]))
        .pop()
    )


badge_value = lambda lines: char_to_value(find_badge(lines))
