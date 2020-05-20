#!/usr/bin/env python
import sys
sys.path.append("..")

from mytools import tools
start = tools.read_file("line")

def get_parameter_list(mylist: list):
    fly_patthern = []
    for el in mylist:
        each = el.rstrip().split(" ")
        fly_patthern.append([int(each[3]), int(each[6]), int(each[-2])])
    print("fly patterns: ", fly_patthern)
    return fly_patthern

def get_distance(race_seconds: int, fly_pattern: list):
    cycle_seconds = fly_pattern[1] + fly_pattern[2]
    cycle_distance = fly_pattern[0] * fly_pattern[1]
    total_cycle, remains =  divmod(race_seconds, cycle_seconds)
    if remains < fly_pattern[1]:
        total_distance = cycle_distance * total_cycle + fly_pattern[0] * remains
    else:
        total_distance = cycle_distance * (total_cycle + 1)
    return total_distance

def main(race_seconds: int):
    results = []
    fly_pattern_list = get_parameter_list(start)
    for fly_pattern in fly_pattern_list:
        r = get_distance(race_seconds, fly_pattern)
        results.append(r)
    result = max(results)
    print(result)
    return result

main(2503)

