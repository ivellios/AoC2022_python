import os


class Processor:
    def __init__(self, size=0):
        self.size = size
        self.res_rows = []
        self.cols = [list() for _ in range(self.size)]
        self.res_cols = [list() for _ in range(self.size)]
        self.result = [list() for _ in range(self.size)]

    def print(self, data):
        for line in data:
            for i in line:
                print(i, end="")
            print("")

    def process(self):
        for i, col in enumerate(self.cols):
            self.res_cols[i] = self.process_col(col)

        self.res_cols = self.cols_to_rows(self.res_cols)

        res = self.sum_all(self.union(self.res_rows, self.res_cols))
        return res

    def process_file_data(self, filename):
        with open(filename, "r+") as f:
            while True:
                data = f.readline()
                if not data:
                    break
                line = data.rstrip(os.linesep)
                row_data = [int(char) for char in line]
                self.res_rows.append(self.process_row(row_data))

        return self.process()

    def process_row(self, data: list[int], build_cols=True):
        result = []
        max = -1
        last_pos = len(data) - 1
        max_pos = 0
        for i, v in enumerate(data):
            if v >= max:
                max_pos = i
            if v > max:
                max = v
                result.append(1)
            else:
                result.append(0)

            # building columns btw
            if build_cols:
                self.cols[i].append(v)

        max = -1
        data1 = list(enumerate(reversed(data[max_pos:])))
        for i, v in data1:
            if v > max:
                max = v
                result[last_pos - i] = 1
            else:
                result[last_pos - i] = 0

        return result

    def process_col(self, line: list[int]):
        return self.process_row(line, False)

    def cols_to_rows(self, cols):
        return tuple(zip(*cols[::1]))

    def union(self, it1, it2):
        for i, l in enumerate(it1):
            self.result[i] = [v or it2[i][j] for j, v in enumerate(l)]

        return self.result

    def sum_all(self, data: list[list[bool]]):
        return sum(sum(line) for line in data)
