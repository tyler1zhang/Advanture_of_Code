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


def day2part1():
    password_list = read_file("2", "list")
    valid_password_counter = 0
    for password in password_list:
        policy_limit = re.findall(r'\d+', password)
        policy_word = re.search(r'\w:', password).group()[0]
        password_str = password.split()[-1]
        repeat_num = password_str.count(policy_word)
        if repeat_num <= int(policy_limit[1]) and repeat_num >= int(policy_limit[0]):
            valid_password_counter += 1
    return valid_password_counter


def day2part2():
    password_list = read_file("2", "list")
    valid_password_counter = 0
    for password in password_list:
        policy_limit = re.findall(r'\d+', password)
        policy_word = re.search(r'\w:', password).group()[0]
        password_str = password.split()[-1]
        if password_str[int(policy_limit[0]) - 1] == policy_word and password_str[int(policy_limit[1]) - 1] != policy_word:
            valid_password_counter += 1
        elif password_str[int(policy_limit[0]) - 1] != policy_word and password_str[int(policy_limit[1]) - 1] == policy_word:
            valid_password_counter += 1
    return valid_password_counter


if __name__ == "__main__":
    print(day2part2())
    # print(day1part2())
