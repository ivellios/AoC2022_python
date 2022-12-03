def string_to_set(string: str):
    return set([*string])


def char_to_value(char):
    char_val = ord(char)
    if char_val in range(ord("A"), ord("Z") + 1):
        return char_val - ord("A") + 27
    if char_val in range(ord("a"), ord("z") + 1):
        return char_val - ord("a") + 1
