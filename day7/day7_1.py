from .day7 import processor_factory


def run(filename):
    p = processor_factory(filename)

    res = p.get_dirs_size_below(100000)
    print("Result: ", res)
    return res


run.no_file_wrapping = True
