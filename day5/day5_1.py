from .day5 import process_move_cratemover9000, process_move


def run(filename):
    process_move(filename, process_move_cratemover9000)

run.no_file_wrapping = True
