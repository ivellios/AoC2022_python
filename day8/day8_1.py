from .day8 import Processor


def run(filename):
    p = Processor(size=99)

    res = p.process_file_data(filename)
    print("Result: ", res)
    return res


run.lines_to_read = 1
run.answer_text = "Total: "
run.no_file_wrapping = True
