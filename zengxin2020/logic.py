import sys
import hashlib
import string
import re
import itertools
import json
import math
import collections
from util import read_file
from functools import reduce
sys.path.append("./lib")

# ############################ Day 1 ##############################
def day1part1():
    mystring = read_file("1", "string")
    floor = 0
    for i in mystring:
        if i == '(':
            floor += 1
        elif i ==')':
            floor -= 1
    return floor

def day1part2():
    floor = 0
    mylist = read_file("1", "list")
    list_floor = tuple(mylist[0])
    for index, value in enumerate(list_floor): 
        if value == '(':
            floor += 1
        elif value ==')':
            floor -= 1
            if floor ==-1: 
                return index+1


if __name__ == "__main__":
    print(day1part2())
