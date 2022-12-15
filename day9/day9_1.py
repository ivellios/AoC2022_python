import os
from typing import List


def is_head_distancing_from_tail(position_head, position_tail):
    hx, hy = position_head
    tx, ty = position_tail
    dist_x = abs(tx-hx)
    dist_y = abs(ty-hy)

    if dist_x == 0 and dist_y == 0:
        return False

    if abs(dist_x + dist_y) <= 2 and (dist_x <= 1 and dist_y <= 1):
        return False

    if abs(dist_x + dist_y) >= 2:
        return True


class Processor:

    POSITION_MAPPING = {
        "U": [0, 1],
        "D": [0, -1],
        "L": [-1, 0],
        "R": [1, 0],
    }

    def __init__(self):
        self.positions = set()
        self.lines = []
        self.head_pos = [0, 0]
        self.tail_pos =[0, 0]
        self.positions.add(self.pos_to_string(self.tail_pos))

    def load_data(self, filename):
        with open(filename, "r+") as f:
            while True:
                data = f.readline()
                if not data:
                    break
                line = data.rstrip(os.linesep)
                self.lines.append(line)

    @property
    def result(self):
        return len(self.positions)

    def process(self):
        for line in self.lines:
            self.process_line(line)

        return self.result

    def pos_to_string(self, pos: List[int]):
        return f"{pos[0]}:{pos[1]}"

    def get_new_pos(self, current_pos, movement_vector):
        return [cur_val+new_val for cur_val,new_val in zip(current_pos, movement_vector)]

    def process_line(self, line: str):
        direction, length = line.split(" ")
        length = int(length)

        for _ in range(length):
            head_old_pos = self.head_pos
            self.head_pos = self.get_new_pos(self.head_pos, self.POSITION_MAPPING[direction])
            if is_head_distancing_from_tail(self.head_pos, self.tail_pos):
                self.tail_pos = head_old_pos
                self.positions.add(self.pos_to_string(self.tail_pos))


p = Processor()

def run(filename):
    p = Processor()
    p.load_data(filename)
    p.process()
    print("Amount of tail positions: ", p.result)


run.lines_to_read = 1
run.answer_text = "Total: "
run.no_file_wrapping = True
