
'''
use import as handler, import all scripts from a folder
user input a folder to hold input
separate the handler
try to use the cpripper structure to do

put all script together in one script like bird do, then use handle separate, and data seperate
'''

import sys
import json
from util import read_file
import logic
import time
sys.path.append("./lib")

with open("./test.json") as f:
    event = json.load(f)
f.close()
# print(event)

function_mapping = {
    "day1part1": logic.day1part1,
    "day1part2": logic.day1part2,
    "day2part1": logic.day2part1,
    "day2part2": logic.day2part2,
    "day3part1": logic.day3part1,
    "day3part2": logic.day3part2,
    "day4part1": logic.day4part1,
    "day4part2": logic.day4part2,
    "day5part1": logic.day5part1,
    "day5part2": logic.day5part2,
    "day6part1": logic.day6part1,
    "day6part2": logic.day6part2,
    "day7part1": logic.day7part1,
    "day7part2": logic.day7part2,
    "day8part1": logic.day8part1,
    "day8part2": logic.day8part2,
    "day9part1": logic.day9part1,
    "day9part2": logic.day9part2,
    "day10part1": logic.day10part1,
    "day10part2": logic.day10part2,
    "day11part1": logic.day11part1,
    "day11part2": logic.day11part2,
    "day12part1": logic.day12part1,
    "day12part2": logic.day12part2,
    "day13part1": logic.day13part1,
    "day13part2": logic.day13part2,
    "day14part1": logic.day14part1,
    "day14part2": logic.day14part2,
    "day15part1": logic.day15part1,
    "day15part2": logic.day15part2,
    "day16part1": logic.day16part1,
    "day16part2": logic.day16part2,
    "day17part1": logic.day17part1,
    "day17part2": logic.day17part2,
    "day18part1": logic.day18part1,
    "day18part2": logic.day18part2,
    "day19part1": logic.day19part1,
    "day19part2": logic.day19part2,
    "day20part1": logic.day20part1,
    "day20part2": logic.day20part2,
    "day21part1": logic.day21part1,
    "day21part2": logic.day21part2,
    "day22part1": logic.day22part1,
    "day22part2": logic.day22part2,
    "day23part1": logic.day23part1,
    "day23part2": logic.day23part2,
    "day24part1": logic.day24part1,
    "day24part2": logic.day24part2,
    "day25part1": logic.day25part1,
    "day25part2": logic.day25part2
}

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': json.dumps({"result": err}) if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    try:
    # parse event and get ready for function mapping
        day = event["queryStringParameters"]["day"]
        question = event["queryStringParameters"]["question"]
        run_func = f"day{day}part{question}"
    except Exception as e:
        return  respond(f"{e} query not included")

    # try to run function
    try: 
        start_time = time.time()  
        result = function_mapping[run_func]()
        running_time = time.time() - start_time
        res = {"result": result, "running_time": running_time}
        return respond(None, res)
    except Exception as e:
        return respond(f"error occured as {e}")
