#!/usr/bin/env python
import re
import sys
sys.path.append("..")
from mytools import tools

start_list = tools.read_file("line")

message = {"children": 3,
           "cats": 7,
           "samoyeds": 2,
           "pomeranians": 3,
           "akitas": 0,
           "vizslas": 0,
           "goldfish": 5,
           "trees": 3,
           "cars": 2,
           "perfumes": 1}

def one(input):
    one_message = {}
    for k, v in message.items():
        one_message[k] = str(v)

    for line in input:
        mylist = re.split(": |, ", line)
        it = iter(mylist[1:])
        rec_dict = dict(zip(it, it))
        if rec_dict.items() <= one_message.items():
            print("the 1st match is: ", line)
            return line

one(start_list)

# question 2
def two(input):
    for line in input:
        mylist = re.split(": |, ", line)
        it = iter(mylist[1:])
        rec_dict = dict(zip(it, it))
        
        match = True
        for k,v in rec_dict.items():
            if k in ["children", "samoyeds", "akitas", "vizslas", "cars", "perfumes"]: 
                if message[k] != int(v):
                    match = False
                    break
            elif k in ["cats", "trees"]:
                if message[k] >= int(v):
                    match = False
                    break
            elif k in ["pomeranians", "goldfish"]:
                if message[k] <= int(v):
                    match = False
                    break
        if match:
            print("the 2nd match is: ", line)
            return line

two(start_list)