# -*- coding: utf-8 -*-
import requests
from pycookiecheat import chrome_cookies #pip3 install pycookiecheat
from solution_2015 import *


def get_input(question_num, year='2016'):
    '''
    To retrieve question input with param: year and question number
    To invoke this function, login onto Github with chrome is a must  
    '''
    input_url='https://adventofcode.com/'+year+'/day/'+question_num+'/input'
    cookies = chrome_cookies(input_url)    
    content = requests.get(input_url, cookies=cookies).text
    return content

def save_input_local():
    '''
    save all input to loca path input/q%d_2015.txt
    '''
    for i in range(1, 26):
        f = open("input/q%d_2016.txt"%i, "w")
        f.write(get_input(str(i)))
        f.close()

def save_exe_time():
    '''
    measure execution time for all solutions and save to execution_time.txt
    '''
    exe_time=[]
    for i in range(1, 26):
        start_time=time.time()  
        exec('q%d_2015_part1()'%i)
        end_time1=time.time()
        exec('q%d_2015_part2()'%i)
        end_time2=time.time()
        exe_time.append((end_time1-start_time, end_time2-end_time1))
    
    f = open("execution_time.txt", "w")
    f.write ("Day Part1  Part2\n")
    i=0
    for part1, part2 in exe_time:
        i+=1
        f.write ("{:02}  {:5.2f}  {:5.2f}\n".format(i, part1, part2))

    f.close()

#### 1.save all input to local path input/qXX_2015.txt  ####
#save_input_local()

#### 2.execute all solutions and save execution time to execution_time.txt
#save_exe_time()



    