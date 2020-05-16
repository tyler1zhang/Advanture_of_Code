#!/usr/bin/env python
import sys
sys.path.append("..")
import re
from mytools import tools

start_list = tools.read_file("line")

def get_parameter_list(mylist: list):
    parameters = []
    for el in mylist:
        numbers = re.findall(r'-?\d+', el)
        parameters.append(list(map(lambda el: int(el), numbers)))
    print("parameters: ", parameters)
    return parameters

def cal_score(parameters: list, recipe: list):
    total_score = 0
    # get the property to iterate first, for exmaple capcity as the first i, leave the calories
    properties = len(parameters[0]) - 1
    total_score = 1
    for i in range(properties):
        property_score = 0
        for j in range(len(recipe)):
            property_score += parameters[j][i] * recipe[j]
        if property_score < 0:
            property_score = 0
        total_score *= property_score
    return total_score


def cal_recipi_combination_score(parameters):
    # the ingredients type is 4, so the recipe here is 4, so to for loop 4 times
    for i in range(101):
        for j in range(101-i):
            for k in range(101-i-j):
                for l in range(101-i-j-k):
                    recipe = [i, j, k, l]
                    recipe_score = cal_score(parameters, recipe)
                    yield recipe_score
def main(input):
    parameters = get_parameter_list(input)
    final_score = cal_recipi_combination_score(parameters)
    # print(list(final_score))
    highest_score = max(final_score)
    print(highest_score)

if __name__ == '__main__': main(start_list)
