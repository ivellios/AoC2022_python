from .dayX import process


def run(line: str):
    return process(line)


run.lines_to_read = 1
run.answer_text = "Total: "
