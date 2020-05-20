import sys
sys.path.append("..")
import itertools
import time

from mytools import tools
START_LIST = tools.read_file("line")

def get_max_min(num_list):
    num_list.sort()
    for i in range(len(num_list)):
        if sum(num_list[:i+1]) == 150:
            max_n = i+1
            break
        elif sum(num_list[:i+1]) > 150:
            max_n = i
            break
    num_list.sort(reverse=True)
    for i in range(len(num_list)):
        if sum(num_list[:i+1]) >= 150:
            min_n = i+1
            break
    return max_n, min_n

def one(my_input):
    """main function"""
    result = 0
    num_list = [int(i) for i in my_input]
    max_n, min_n = get_max_min(num_list)
    print(max_n, min_n)
    for i in range(min_n, max_n+1):
        combination = itertools.combinations(num_list, i)
        for j in combination:
            # print(f"i is {i}, j is {j} sum is {sum(j)}")
            if sum(j) == 150:
                result += 1
    print("the 1st result is ", result)
    return result

start_time = time.time()
one(START_LIST)
print(time.time() - start_time)

def two(my_input):
    result = 0
    num_list = [int(i) for i in my_input]
    max_n, min_n = get_max_min(num_list)
    combination = itertools.combinations(num_list, min_n)
    for j in combination:
        if sum(j) == 150:
            result += 1
    print("the 2nd result is ", result)
    return result

two(START_LIST)
