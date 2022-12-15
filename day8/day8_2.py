import os


class Processor:

    def __init__(self):
        self.trees_map = []

    def process_file_data(self, filename):
        with open(filename, "r+") as f:
            while True:
                data = f.readline()
                if not data:
                    break
                line = data.rstrip(os.linesep)
                row_data = [int(char) for char in line]
                self.trees_map.append(row_data)
        return self.process()


    def process(self):
        self.row_size = len(self.trees_map[0])
        self.col_size = len(self.trees_map)
        self.results_map = [[0]*self.row_size]*self.col_size
        res = 0

        for index_y, row in enumerate(self.trees_map): # 1, 225512
            if index_y == 0 or index_y == self.row_size - 1:
                continue

            for index_x, tree in enumerate(row): # 2, 5

                if index_x == 0 or index_y == self.row_size - 1:
                    continue

                length_x_r = 0
                for a_tree in range(index_x + 1, self.row_size): # 3, 4
                    length_x_r += 1
                    if row[a_tree] >= tree:
                        break
                # 2

                length_x_l = 0
                for a_tree in range(index_x - 1, -1, -1): # 1, 0, -1
                    length_x_l += 1
                    if row[a_tree] >= tree:
                        break
                # 1

                length_y_u = 0
                for a_tree in range(index_y - 1, -1, -1): # 0
                    length_y_u += 1
                    if self.trees_map[a_tree][index_x] >= tree:
                        break
                # 1

                length_y_d = 0
                for a_tree in range(index_y + 1, self.col_size): # 2, 3, 4
                    length_y_d += 1
                    if self.trees_map[a_tree][index_x] >= tree:
                        break
                # 2

                field = length_y_u * length_y_d * length_x_l * length_x_r
                res = field if field > res else res

        return res


def run(filename):
    p = Processor()
    res = p.process_file_data(filename)
    print("RESULT: ", res)
    return res


run.lines_to_read = 1
run.answer_text = "Result: "
run.no_file_wrapping = True
