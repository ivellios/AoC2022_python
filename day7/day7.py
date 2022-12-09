import json


class Processor:

    def __init__(self):
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
            values = line.split(' ')
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
