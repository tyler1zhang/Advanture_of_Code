import requests
from pycookiecheat import chrome_cookies #pip3 install pycookiecheat

###########  Global Function  #############

#To retrieve question input with param: year and question number
#To invoke this function, login onto Github with chrome is a must 
def get_input(question_num, year='2015'):
    input_url='https://adventofcode.com/'+year+'/day/'+question_num+'/input'
    cookies = chrome_cookies(input_url)    
    content = requests.get(input_url, cookies=cookies).text
    return content

###########  Starting of Solution  #############

def q1_2015_part1():
    '''
        An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
        The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.   
        For example:   
        (()) and ()() both result in floor 0.
        ((( and (()(()( both result in floor 3.
        ))((((( also results in floor 3.
        ()) and ))( both result in floor -1 (the first basement level).
        ))) and )())()) both result in floor -3.
        To what floor do the instructions take Santa?
    '''
    input=get_input('1','2015')
    answer= input.count('(')-input.count(')')
    return answer

def q1_2015_part2():
    '''
        Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). 
        The first character in the instructions has position 1, the second character has position 2, and so on.
    '''
    input=get_input('1','2015')
    for index in range(len(input)):
        current_floor=input.count('(',0,index)-input.count(')',0,index)
        #print(index, current_floor)
        if current_floor==-1:
            return index

###########  Execution  #############
print(q1_2015_part2())