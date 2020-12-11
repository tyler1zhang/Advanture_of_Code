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


def day3part1():
    tree_map = read_file("3", "list")
    one_line_round = (len(tree_map[0]) - 1) // 3
    total_round_need = (len(tree_map) // one_line_round) + 1
    tree_counter = 0
    for i, el in enumerate(tree_map):
        repeat_el = el * total_round_need
        if repeat_el[3 * i] == "#":
            tree_counter += 1
    return tree_counter

def day3part2():
    tree_map = read_file("3", "list")
    one_line_round = (len(tree_map[0]) - 1) // 7
    total_round_need = (len(tree_map) // one_line_round) + 1
    tree_counter = [0, 0, 0, 0, 0]
    for i, el in enumerate(tree_map):
        repeat_el = el * total_round_need
        if repeat_el[i] == "#":
            tree_counter[0] += 1
        if repeat_el[3 * i] == "#":
            tree_counter[1] += 1
        if repeat_el[5 * i] == "#":
            tree_counter[2] += 1
        if repeat_el[7 * i] == "#":
            tree_counter[3] += 1
        if i % 2 == 0:
            if repeat_el[int(i / 2)] == "#":
                tree_counter[4] += 1
    print(tree_counter)
    product = functools.reduce(lambda a,c: a*c, tree_counter)
    return product


def day4part1():
    passport_records = read_file("4", "string")
    passport_records_list = passport_records.split("\n\n")
    valid_passport_counter = 0
    for passport_record in passport_records_list:
        if re.match(r"(?=(.|\s)*byr)(?=(.|\s)*iyr)(?=(.|\s)*eyr)(?=(.|\s)*hgt)(?=(.|\s)*hcl)(?=(.|\s)*ecl)(?=(.|\s)*pid)", passport_record):
            valid_passport_counter += 1
    return valid_passport_counter

def day4part2():
    passport_records = read_file("4", "string")
    passport_records_list = passport_records.split("\n\n")
    valid_passport_counter = 0
    for passport_record in passport_records_list:
        # print(passport_record)
        # print()
        if re.match(r"(?=(.|\s)*byr:(19[2-9][0-9]|200[0-2])(\s|$))(?=(.|\s)*iyr:(201[0-9]|2020)(\s|$))(?=(.|\s)*eyr:(202[0-9]|2030)(\s|$))(?=(.|\s)*hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)(\s|$))(?=(.|\s)*hcl:#[0-9,a-f]{6}(\s|$))(?=(.|\s)*ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$))(?=(.|\s)*pid:[0-9]{9}(\s|$))", passport_record):
            valid_passport_counter += 1
            print("aaaaaaaaaaaaaaaaaaaaaaa", passport_record)
            # print()
            print()
    return valid_passport_counter


if __name__ == "__main__":
    # print(day4part1())
    print(day4part2())
