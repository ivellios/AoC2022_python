from day1.day1 import run as run_day1
from day2.day2_1 import run as run_day2_1
from day2.day2_2 import run as run_day2_2
from day3.day3_1 import rucksacks as rucksacks_1
from day3.day3_2 import rucksacks as rucksacks_2
from day4.day4_1 import duties_containing
from day4.day4_2 import duties_overlapping

print("======= Day 1 1+2 =======")
run_day1("data/day1.txt")
print("======= Day 2 - 1 =======")
run_day2_1("data/day2.txt")
print("======= Day 2 - 2 =======")
run_day2_2("data/day2.txt")
print("======= Day 3 - 1 =======")
rucksacks_1("data/day3.txt")
print("======= Day 3 - 2 =======")
rucksacks_2("data/day3.txt")
print("======= Day 4 - 1 =======")
duties_containing("data/day4.txt")
print("======= Day 4 - 1 =======")
duties_overlapping("data/day4.txt")
