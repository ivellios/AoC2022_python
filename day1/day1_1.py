import os


def run(filename):
    max_num = 0
    sum_num = 0

    max_1 = 64929
    max_2 = 36522
    max_3 = 62518

    sums = []
    with open(filename, "r+") as f:
        while True:
            data = f.readline()
            if not data:
                break

            d = data.rstrip(os.linesep)
            if d:
                sum_num += int(d)
            else:
                sums.append(sum_num)
                sum_num = 0

        sums.sort()
        print(sums[-1], sums[-2], sums[-3], sums[-3] + sums[-2] + sums[-1])


run.no_file_wrapping = True
