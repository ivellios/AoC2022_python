from day1.day1 import run as run_day1
from day2.day2_1 import choice_result_value
from day2.day2_2 import pick_choice_result
from day3.day3_1 import rucksack_reorganization
from day3.day3_2 import badge_value
from day4.day4_1 import check_bad_duties
from day4.day4_2 import check_duty_overlapping
from utils import run_with_file

print("======= Day 1 1+2 =======")
run_day1("data/day1.txt")
print("======= Day 2 - 1 =======")
run_with_file(choice_result_value, "data/day2.txt")
print("======= Day 2 - 2 =======")
run_with_file(pick_choice_result, "data/day2.txt")
print("======= Day 3 - 1 =======")
run_with_file(rucksack_reorganization, "data/day3.txt")
print("======= Day 3 - 2 =======")
run_with_file(badge_value, "data/day3.txt", lines_to_read=3)
print("======= Day 4 - 1 =======")
run_with_file(check_bad_duties, "data/day4.txt")
print("======= Day 4 - 1 =======")
run_with_file(check_duty_overlapping, "data/day4.txt")
