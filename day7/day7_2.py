from .day7 import processor_factory


def run(filename):
    p = processor_factory(filename, size=70000000, update_size=30000000)
    res = p.get_most_fitting_dir_size()
    print("Result: ", res)
    return res


run.no_file_wrapping = True
