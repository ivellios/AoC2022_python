import json
import os
from pprint import pprint


class Processor:
    def __init__(self, size=0, update_size=0):
        self.size = size
        self.update_size = update_size
        self.tree = dict()
        self.curdir = []

    @property
    def cur(self):
        return json.dumps(self.curdir)

    @property
    def prev(self):
        return json.dumps(self.curdir[-1])

    def process(self, line):
        if line == "$ ls":
            return
        elif line.startswith("dir"):
            return
        elif line == "$ cd ..":
            print("Going out ", self.cur)
            cur_sum = self.tree[self.cur]
            self.curdir = self.curdir[:-1]
            self.tree[self.cur] += cur_sum  # add sum of subdir
            print("Gone out ", self.cur)
        elif line.startswith("$ cd "):
            newdir = line[5:]
            self.curdir.append(newdir)
            self.tree[self.cur] = 0
            print("Going in ", self.cur)
        else:
            values = line.split(" ")
            size = int(values[0])
            print("Adding ", size)
            self.tree[self.cur] += size

    def process_to_root(self):
        print(self.tree)
        while len(self.curdir):
            dir = self.cur
            if dir == '["/"]':
                break
            print(self.curdir, dir)
            dir_sum = self.tree[dir]
            print(dir_sum, self.tree[self.cur])
            self.curdir = self.curdir[:-1]
            self.tree[self.cur] += dir_sum
            print(self.tree[self.cur])

    def get_dirs_size_below(self, threshold: int):
        return sum(self.tree[dir] for dir in self.tree if self.tree[dir] <= threshold)

    def get_sorted_tree(self):
        return sorted(
            [(key, self.tree[key]) for key in self.tree], key=lambda element: element[1]
        )

    @property
    def free_space(self):
        return self.size - self.tree['["/"]']

    @property
    def space_needed(self):
        return self.update_size - self.free_space

    def get_most_fitting_dir_size(self):
        sorted_tree = self.get_sorted_tree()
        pprint(sorted_tree)

        filtered_tree = list(
            filter(lambda element: element[1] >= self.space_needed, sorted_tree)
        )

        return filtered_tree[0][1]


def processor_factory(filename, size=0, update_size=0):
    p = Processor(size=size, update_size=update_size)
    with open(filename, "r+") as f:
        while True:
            data = f.readline()
            if not data:
                break
            line = data.rstrip(os.linesep)
            pprint(line)
            p.process(line)

    p.process_to_root()

    return p
