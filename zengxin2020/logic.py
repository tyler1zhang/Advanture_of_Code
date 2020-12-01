import sys
import hashlib
import string
import re
import itertools
import functools
import json
import math
import collections
from util import read_file
from functools import reduce
sys.path.append("./lib")

# ############################ Day 1 ##############################
def day1part1():
    entity_list = read_file("1", "list")
    for entity in entity_list:
        sub_entity = 2020 - int(entity)
        if str(sub_entity) in entity_list:
            return int(entity) * sub_entity

def day1part2():
    entity_list = read_file("1", "list")
    entity_list_num = [int(x) for x in entity_list]
    combination_three = itertools.combinations(entity_list_num, 3)
    for el in combination_three:
        if sum(el) == 2020:
            return functools.reduce(lambda a, b: a * b, el)


if __name__ == "__main__":
    print(day1part1())
    print(day1part2())
