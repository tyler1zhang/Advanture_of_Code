#!/usr/bin/env python
import sys
sys.path.append("..")

from mytools import tools
start = tools.read_file("line")

def get_parameter_list(mylist: list):
    fly_patthern = []
    for el in mylist:
        each = el.rstrip().split(" ")
        # add name to fly pattern for future points given
        fly_patthern.append([int(each[3]), int(each[6]), int(each[-2]), each[0]])
    return fly_patthern

def get_distance(race_seconds: int, fly_pattern: list):
    cycle_seconds = fly_pattern[1] + fly_pattern[2]
    cycle_distance = fly_pattern[0] * fly_pattern[1]
    total_cycle, remains =  divmod(race_seconds, cycle_seconds)
    if remains < fly_pattern[1]:
        total_distance = cycle_distance * total_cycle + fly_pattern[0] * remains
    else:
        total_distance = cycle_distance * (total_cycle + 1)
    # get the name and distance at each second
    return fly_pattern[-1], total_distance

def get_name(race_seconds: int):
    winner_names = {}
    fly_pattern_list = get_parameter_list(start)
    for fly_pattern in fly_pattern_list:
        name, total_distance = get_distance(race_seconds, fly_pattern)
        winner_names[name] = total_distance
    
    # get the winner name for each second
    winner_name = [key for key, value in winner_names.items() if value == max(winner_names.values())]
    return winner_name[0]

def main(totol_seconds: int):
    winner_name_scoreboard = {}
    for i in range(totol_seconds):
        winner = get_name(i+1)
        if winner in winner_name_scoreboard:
            winner_name_scoreboard[winner] += 1  
        else:
            winner_name_scoreboard[winner] = 1
    print("final scoreboard: ", winner_name_scoreboard)
    print("highest: ", max(winner_name_scoreboard.values()))
        
main(2503)


