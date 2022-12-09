import json


class Processor:

    def __init__(self):
        self.tree = dict()
        self.curdir = []

    def process(self, line):
        if line == "$ ls":
            return
        elif line.startswith("dir"):
            return
        elif line == "$ cd ..":
            print("Going out ", self.curdir)
            cur_sum = self.tree[self.curdir[-1]]
            self.curdir = self.curdir[:-1]
            # cd = json.dumps(self.curdir)
            # curdir = json.loads(self.cd)
            self.tree[self.curdir[-1]] += cur_sum  # add sum of subdir
            print("Gone out ", self.curdir)
        elif line.startswith("$ cd "):
            newdir = line[5:]
            self.curdir.append(newdir)
            self.tree[self.curdir[-1]] = 0
            print("Going in ", self.curdir)
        else:
            values = line.split(' ')
            size = int(values[0])
            print("Adding ", size)
            self.tree[self.curdir[-1]] += size

    def process_to_root(self):
        for dir in reversed(self.curdir):
            if dir == "/":
                continue
            print(self.curdir, dir)
            dir_sum = self.tree[dir]
            print(dir_sum, self.tree[self.curdir[-1]])
            self.curdir = self.curdir[:-1]
            self.tree[self.curdir[-1]] += dir_sum
            print(self.tree[self.curdir[-1]])

    def get_dirs_size_below(self, threshold: int):
        return sum(self.tree[dir] for dir in self.tree if self.tree[dir] <= threshold)
