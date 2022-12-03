opponent_choices = {
    "A": 1,  # rock
    "B": 2,  # paper
    "C": 3,  # scissors
}

my_choices = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

WIN = 6
DRAW = 3
LOSE = 0

RESULTS = [
    [DRAW, LOSE, WIN],
    [WIN, DRAW, LOSE],
    [LOSE, WIN, DRAW],
]

LOSE_MAP = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

WIN_MAP = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}

DRAW_MAP = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}


expected_results = {
    "X": LOSE,  # lose
    "Y": DRAW,  # draw
    "Z": WIN,  # win
}
