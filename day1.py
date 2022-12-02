import os

max_num = 0
sum_num = 0

max_1 = 64929
max_2 = 36522
max_3 = 62518

sums = []
with open("day1.txt", "r+") as f:
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
            # max_num = max(max_num, sum_num)
            # if max_num != max_1 and max_num <= max_2:
            #     # max_2 = sum_num
            #     max_3 = sum_num
            # sum_num = 0
