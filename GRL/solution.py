# -*- coding: utf-8 -*-
import requests
from pycookiecheat import chrome_cookies #pip3 install pycookiecheat
import hashlib 
import re
import time
import json
from tsp_solver.greedy import solve_tsp #pip3 install tsp_solver2
from itertools import permutations, combinations
import copy
from functools import reduce
from math import factorial, ceil
import numpy

###########  Global Function  #############

#To retrieve question input with param: year and question number
#To invoke this function, login onto Github with chrome is a must 
def get_input(question_num, year='2015'):
    f = open("input/q%s_2015.txt"%question_num, "r")
    content=f.read()
    f.close()
    return content

###########  Starting of Solution  #############

####===>  Day 1 Solution <===####
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

####===>  Day 2 Solution <===####        
def q2_2015_part1():
    '''
        Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper 
        for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little 
        extra paper for each present: the area of the smallest side.
        All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
    '''
    input=get_input('2','2015').splitlines()
    total_area=0
    for item in input:
        side=item.split('x')
        side=[int(side[0]),int(side[1]),int(side[2])]
        area1=side[0]*side[1]
        area2=side[0]*side[2]
        area3=side[1]*side[2]
        smallest_area=min(area1, area2, area3)
        total_area+=2*(area1+area2+area3)+smallest_area
        
    return total_area

def q2_2015_part2():
    '''
        The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. 
        Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to 
        the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.
        How many total feet of ribbon should they order?
    '''
    input=get_input('2','2015').splitlines()
    total_area=0
    for item in input:
        side=item.split('x')
        side=[int(side[0]),int(side[1]),int(side[2])]
        largest_side=max(side[0], side[1], side[2])

        total_area+=2*(side[0]+side[1]+side[2])-2*largest_side+side[0]*side[1]*side[2]
        
    return total_area

####===>  Day 3 Solution <===####
def q3_2015_part1():
    '''
        Santa is delivering presents to an infinite two-dimensional grid of houses.He begins by delivering a present to the house at 
        his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are 
        always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present 
        to the house at his new location.
    
        However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa 
        ends up visiting some houses more than once. How many houses receive at least one present?
    '''
    input=get_input('3','2015')
    coordinate_set={'0/0',}
    current_x=0
    current_y=0
    for char in input:
        if char=='^':
            current_y+=1
        elif char=='v':
            current_y-=1
        elif char=='<':
            current_x-=1
        elif char=='>':
            current_x+=1
        coordinate_set.add(str(current_x)+'/'+str(current_y))
    
    return len(coordinate_set)

def q3_2015_part2():
    '''
        Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving 
        based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
        
        This year, how many houses receive at least one present?
    '''
    input=get_input('3','2015')
    coordinate_set={'0/0',}
    santa_x=0
    santa_y=0
    robo_x=0
    robo_y=0
    santa_to_move=True
    
    for char in input:
        if santa_to_move:
            if char=='^':
                santa_y+=1
            elif char=='v':
                santa_y-=1
            elif char=='<':
                santa_x-=1
            elif char=='>':
                santa_x+=1
            coordinate_set.add(str(santa_x)+'/'+str(santa_y))
        else: 
            if char=='^':
                robo_y+=1
            elif char=='v':
                robo_y-=1
            elif char=='<':
                robo_x-=1
            elif char=='>':
                robo_x+=1
            coordinate_set.add(str(robo_x)+'/'+str(robo_y))
        #change turn    
        santa_to_move=not santa_to_move
        
    return len(coordinate_set)   

####===>  Day 4 Solution <===####
def q4_2015_part1():
    return q4_2015(part_num=1)
    
def q4_2015_part2():
    return q4_2015(part_num=2)
    
def q4_2015(part_num=1):  #shared by part 1 and part 2
    '''
    part1:
        To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash 
        is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa 
        the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.       
        For example:        
        If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), 
        and it is the lowest such number to do so.
        If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; 
        that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
        Your puzzle input is bgvyzdsv.
        
    part2:
        Now find one that starts with six zeroes.
    '''
    input='bgvyzdsv'
    suffix=10  #no leading zeroes
    str_to_match='00000' if part_num==1 else '000000'
    
    while True: #Exhaustive search, 穷举 until find the match
        secret_key=input+str(suffix)
        hash = hashlib.md5(secret_key.encode()).hexdigest()
        if hash.startswith(str_to_match):
            return suffix
        suffix+=1

####===>  Day 5 Solution <===#### 
def q5_2015_part1():
    '''
        A nice string is one with all of the following properties:       
        1. It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
        2. It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
        3. It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
        How many strings are nice?
    '''   
    input=get_input('5','2015').splitlines()
    nice_str_count=0
    
    for str_to_check in input: #starting check each line of string
        # check if contain ab, cd, pq, or xy
        if 'ab' in str_to_check or 'cd' in str_to_check or 'pq' in str_to_check or 'xy' in str_to_check:
            continue
        
        vowels_count=0
        appear_twice=False
        previous_char=''
        for current_char in str_to_check: # optimize the iteration
            if current_char in 'aeiou':  #given all input are in lower case
                vowels_count+=1
            if current_char==previous_char:
                appear_twice=True
            previous_char=current_char
        
        if appear_twice and vowels_count>2: # check requirement 1 and 2 fulfilled or not
            nice_str_count+=1
                
    return nice_str_count            

def q5_2015_part2():
    '''
        Now, a nice string is one with all of the following properties:
        
        1. It contains a pair of any two letters that appears at least twice in the string without overlapping, 
        like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
        2. It contains at least one letter which repeats with exactly one letter between them, 
        like xyx, abcdefeghi (efe), or even aaa.   
    '''   
    input=get_input('5','2015').splitlines()
    nice_str_count=0
    
    for str_to_check in input: #starting check each line of string
        
        ## checking requirement 1 ##
        pair_appear_twice=False        
        for index in range(2, len(str_to_check)): 
            # to check if current pair appear in set and not equal previous pair
            if str_to_check[index-2:index] in str_to_check[index:len(str_to_check)]:
                pair_appear_twice=True
                #print(str_to_check[index-1:index+1])
                break
            
        ## checking requirement 2 ##
        appear_inbetween=False        
        for index in range(2, len(str_to_check)): 
            #to check if current char equal to the char 2 position ahead
            if str_to_check[index]==str_to_check[index-2]: 
                appear_inbetween=True
                #print(str_to_check[index-2:index+1])
                break
        # to check if requirement 1 and 2 fulfilled 
        if pair_appear_twice and appear_inbetween:
            nice_str_count+=1
            #print(str_to_check)
            
    return nice_str_count    

####===>  Day 6 Solution <===####
def q6_2015_part1():
    '''
        Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 
        0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle 
        various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners 
        of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in 
        a 3x3 square. The lights all start turned off.
        After following the instructions, how many lights are lit?
    '''
    input=get_input('6','2015').splitlines()  
    status_matrix=[[False for x in range(1000)] for y in range(1000)] 
    
    for line in input:
        # parse instruction param
        instruction=re.findall(r"[\w']+", line)
        y2=int(instruction[-1])
        x2=int(instruction[-2])
        y1=int(instruction[-4])
        x1=int(instruction[-5])
        if line.startswith('turn on'):
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    status_matrix[x][y]=True
        elif line.startswith('turn off'):
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    status_matrix[x][y]=False
        elif line.startswith('toggle'):
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    status_matrix[x][y]=not status_matrix[x][y]
    lit_count=0
    for row in status_matrix:
        lit_count+=row.count(True)
        
    return lit_count

def q6_2015_part2():
    '''
        The phrase turn on actually means that you should increase the brightness of those lights by 1.
        The phrase turn off actually means that you should decrease the brightness of those lights by 1, 
        to a minimum of zero.        
        The phrase toggle actually means that you should increase the brightness of those lights by 2.
        
        What is the total brightness of all lights combined after following Santa's instructions?
    '''
    input=get_input('6','2015').splitlines()  
    status_matrix=[[0 for x in range(1000)] for y in range(1000)] 
    
    for line in input:
        # parse instruction param
        instruction=re.findall(r"[\w']+", line)
        y2=int(instruction[-1])
        x2=int(instruction[-2])
        y1=int(instruction[-4])
        x1=int(instruction[-5])
        if line.startswith('turn on'):
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    status_matrix[x][y]=status_matrix[x][y]+1
        elif line.startswith('turn off'):
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    status_matrix[x][y]=max(0,status_matrix[x][y]-1)
        elif line.startswith('toggle'):
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    status_matrix[x][y]=status_matrix[x][y]+2
    total_brightness=0
    for row in status_matrix:
        for brightness in row:
            total_brightness+=brightness
        
    return total_brightness

####===>  Day 7 Solution <===####
def q7_2015_part1():
    input=get_input('7','2015').splitlines()
    known_signal={} 
    last_known_wire=''
    while True:
        for line in input: ## to find wire with direct knows signal value
            wire=line.split(' -> ')[1]
            signal=line.split(' -> ')[0]
    
            if signal.isnumeric(): # case: 123 -> x
                known_signal[wire]=int(signal)
                last_known_wire=wire
                input.remove(line)
                break
                
            instruction=signal.split()
            if instruction[0]=='NOT' and instruction[1].isnumeric() :  #case: NOT 123 -> h
                known_signal[wire]=int(65535-int(instruction[1]))
                last_known_wire=wire
                input.remove(line)
                break
            #case 123 AND 456 ->h
            elif instruction[0].isnumeric() and instruction[2].isnumeric():
                if instruction[1]=='AND':
                    signal=int(instruction[0])&int(instruction[2])
                if instruction[1]=='OR':
                    signal=int(instruction[0])|int(instruction[2])
                if instruction[1]=='LSHIFT':
                    signal=int(instruction[0])<<int(instruction[2])
                if instruction[1]=='RSHIFT':
                    signal=int(instruction[0])>>int(instruction[2])                    
                
                known_signal[wire]=signal  
                last_known_wire=wire                 
                input.remove(line)  
                break
     
        if last_known_wire=='a': ## to check if wire 'a' value is known
            return  known_signal[wire] 
        
        for index1 in range(len(input)): ## to replace all value-known wire with its value in all circuit
            list=input[index1].split()
            for index in range(len(list)):
                if list[index] == last_known_wire:
                    list[index]=str(known_signal[last_known_wire])
                    input[index1]=' '.join(list) 
            
    #return get_signal(circuit_dict,'a')

#recursively find up-stream of circuit. but will run into infinite loop for some cases
#e.g  b AND c ->a,  e AND f ->b, b AND g ->e, 123 ->g, 45 ->e, 67 ->f
def get_signal(circuit_dict, destination):
    #print('get_signal for ', destination)
    if destination.isnumeric(): # case: 123 
        return int(destination)
    
    instruction=circuit_dict[destination].split()
    #print(circuit_dict[destination],'-->', destination)
    if len(instruction)==1: # case: 123 -> x
        return get_signal(circuit_dict, instruction[0])
    elif instruction[0]=='NOT':  #case: NOT abc -> h
        return 65535-get_signal(circuit_dict, instruction[1])   
    elif instruction[1]=='AND':
        return get_signal(circuit_dict, instruction[0])&get_signal(circuit_dict, instruction[2])    
    elif instruction[1]=='OR':
        return get_signal(circuit_dict, instruction[0])|get_signal(circuit_dict, instruction[2])
    elif instruction[1]=='LSHIFT':
        return get_signal(circuit_dict, instruction[0])<<int(instruction[2])
    elif instruction[1]=='RSHIFT':
        return get_signal(circuit_dict, instruction[0])>>int(instruction[2])    

def q7_2015_part2():
    input=get_input('7','2015').splitlines()
    known_signal={} 
    last_known_wire=''
    while True:
        for line in input: ## to find wire with direct knows signal value
            wire=line.split(' -> ')[1]
            signal=line.split(' -> ')[0]
    
            if signal.isnumeric(): # case: 123 -> x
                known_signal[wire]=int(signal)
                if wire=='b':
                    known_signal[wire]=956
                last_known_wire=wire
                input.remove(line)
                break
                
            instruction=signal.split()
            if instruction[0]=='NOT' and instruction[1].isnumeric() :  #case: NOT 123 -> h
                known_signal[wire]=int(65535-int(instruction[1]))
                last_known_wire=wire
                input.remove(line)
                break
            #case 123 AND 456 ->h
            elif instruction[0].isnumeric() and instruction[2].isnumeric():
                if instruction[1]=='AND':
                    signal=int(instruction[0])&int(instruction[2])
                if instruction[1]=='OR':
                    signal=int(instruction[0])|int(instruction[2])
                if instruction[1]=='LSHIFT':
                    signal=int(instruction[0])<<int(instruction[2])
                if instruction[1]=='RSHIFT':
                    signal=int(instruction[0])>>int(instruction[2])                    
                
                known_signal[wire]=signal  
                last_known_wire=wire                 
                input.remove(line)  
                break
     
        if last_known_wire=='a': ## to check if wire 'a' value is known
            return  known_signal[wire] 
        
        for index1 in range(len(input)): ## to replace all value-known wire with its value in all circuit
            list=input[index1].split()
            for index in range(len(list)):
                if list[index] == last_known_wire:
                    list[index]=str(known_signal[last_known_wire])
                    input[index1]=' '.join(list)  
                           
####===>  Day 8 Solution <===####
## use unicode_escape decoder to decode original str to escape form
## e.g. "\x27" -> "'", however result still retain double colon, need minus 2 for final length 
def q8_2015_part1():
    input=get_input('8','2015').splitlines()
    count_of_code=0
    count_in_memory=0
    for line in input:
        count_of_code+=len(line)
        count_in_memory+=len(bytes(line, "utf-8").decode("unicode_escape"))-2
    
    return count_of_code-count_in_memory

##json.dumps perfectly resolve this problem, e.g. "\x27" -->"\"\\x27\""
def q8_2015_part2():
    input=get_input('8','2015').splitlines()
    count_encoded=0
    count_original=0
    for line in input:
        count_original+=len(line)
        count_encoded+=len(json.dumps(line))
     
    return count_encoded-count_original

####===>  Day 9 Solution <===####
##typical TSP problem, time complexity O(n^2*2^n)
def q9_2015_part1(n=7):
    if n==7:
        input=get_input('9','2015').splitlines()
    else:
        input= generate_input(n)
    dist_matrix=[]
    line_index=-1
    for row in range(n+1): ##build the distance matrix
        dist_list=[]
        for index in range(row):           
            data=input[line_index].split()
            dist_list.append(int(data[4]))
            line_index-=1
        dist_matrix.append(dist_list)    
    ## solve the best path    
    path = solve_tsp(dist_matrix)
    ## calculate total distance
    total_dist=0
    for index in range(1,len(path)):
        total_dist+=dist_matrix[max(path[index-1], path[index])][min(path[index-1], path[index])]
    
    return total_dist

## Exhaustive search, time complexity O(n!), very high
def q9_2015_part2(n=7): 
    if n==7:
        input=get_input('9','2015').splitlines()
    else:
        input= generate_input(n)
    places = set()
    distances = dict()
    for line in input:
        (source, _, dest, _, distance) = line.split()
        places.add(source)
        places.add(dest)
        distances.setdefault(source, dict())[dest] = int(distance)
        distances.setdefault(dest, dict())[source] = int(distance)

    longest = 0
    for record in permutations(places):
        dist = sum(map(lambda x, y: distances[x][y], record[:-1], record[1:]))
        longest = max(longest, dist)
    
    return longest
## to generate input with n+1 cities for simulation purpose
def generate_input(n=7):
    from random import randrange
    input=[]
    for i in range(n):
        for j in range(n-i):
            line='city'+str(i)+' to '+'city'+str(i+j+1)+' = '+str(randrange(100))
            input.append(line)
    return input

####===>  Day 10 Solution <===####
def q10_2015_part1():
    return q10_2015(repeat_count=40)

def q10_2015_part2():
    return q10_2015(repeat_count=50)

def q10_2015(repeat_count): 
    input='1113122113'
    re_digit = re.compile(r'((\d)\2*)') #find repeated digit
    for i in range(repeat_count):
        #print('loop', i)
        input = re_digit.sub(replace,input)
    return len(input)
## replace repeated digits to its 'say' form, e.g 11 -> two 1 -> 21
def replace(match_str): 
    s = match_str.group(1)
    return str(len(s)) + s[0]
##this function takes too long to run 50 times. improved to replace() above   
def get_next(seq): 
    k,last,result = 1,seq[0],''
    for i in range(1,len(seq)):
        if last==seq[i]:
            k+=1
        else:
            result = result+str(k)+last
            k=1
        last = seq[i]
    result = result+str(k)+last
    return result

####===>  Day 11 Solution <===####
def q11_2015_part1():
    pw =get_input('11','2015').splitlines()[0]
    while not is_pw_valid(pw):
        pw=password_increment(pw)
    return pw

def q11_2015_part2():
    pw =password_increment(q11_2015_part1())
    while not is_pw_valid(pw):
        pw=password_increment(pw)
    return pw

def password_increment(pw): #create new pw by increment 1
    pw+='a'   # append 'a' to end
    for i in range(1, len(pw)): #check if ending with i 'a'
        if pw[-i:].count('a')==i:
            increment=2 if pw[-i-1] in {'h','n','k'} else 1 # char before i, o, l
            new_letter=chr(ord(pw[-i-1]) + increment) if pw[-1-i]!='z' else 'a'
            pw=pw[:len(pw)-i-1] + new_letter+pw[len(pw)-i:]
    return pw[:len(pw)-1] # remove appended 'a'
def is_pw_valid(pw):
    ##checking letter pairs
    pairs_set=set()
    for index in range(1, len(pw)):
        if pw[index-1]!=pw[index]:
            continue
        else: pairs_set.add(pw[index])
    if len(pairs_set)<2: return False    
    ##checking straight increasing like bcd
    for index in range(2, len(pw)):
        if ord(pw[index])-ord(pw[index-1])==1 and ord(pw[index-1])-ord(pw[index-2])==1:
            return True    
    return False    

####===>  Day 12 Solution <===####
## fastest way, cheating by split whole input string, find all numeric item and sum up
def q12_2015_part1():
    input=get_input('12', '2015')
    data= re.split(':|\s|\n|\[|\]|{|}|,|"',input)
    sum=0
    for item in data:
        if item.isnumeric() or (item.startswith('-') and item[1:].isnumeric()):
            sum+=int(item)
    return sum

def q12_2015_part2():
    input=get_input('12', '2015')
    json_obj=json.loads(input)
    data_list=[]
    sum=0
    object_to_list(json_obj, data_list) # convert json object to list
    for item in data_list:
        if isinstance(item, int):
            sum+=int(item)
    return sum
## convert json object to list(1d array)
def object_to_list(obj, data_list):
    ## case of obj is dict
    if isinstance(obj, dict):
        ##pre-check if any item with value 'red', then ignore this dict
        for key, value in obj.items():
            if value=='red':
                return 
        ## no 'red' value, then add each value to data_list          
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                object_to_list(value, data_list)
            else:
                data_list.append(value)
    ## case of obj is list
    elif isinstance(obj, list):
        ## add each item to data_list
        for item in obj:
            if isinstance(item, (dict, list)):
                object_to_list(item, data_list)
            else:
                data_list.append(item)
                
####===>  Day 13 Solution <===####                
## Exhaustive permutations, time complexity O(n!), very high
def q13_2015_part1(): 
    input=get_input('13', '2015').splitlines()
    guest_set = set()
    happiness_dict = dict()
    for line in input: #construct data structure
        data = line.split()
        source=data[0]
        dest=data[10].replace('.', '')
        happiness=int(data[3]) if data[2]=='gain' else -int(data[3])
        guest_set.add(source)
        guest_set.add(dest)
        happiness_dict.setdefault(source, dict())[dest] = happiness
    
    ##there is no difference for rotating the table seating. however it's considered as different case in permutations
    ##so remove one guest from set for permutations and add him back to end of permutations for calculate happiness
    ##this way will reduce time complexity from n to n-1
    last_guest=source  
    guest_set.remove(last_guest)
    optimal_happiness =0
    for record in permutations(guest_set):
        total_happiness = 0
        record+=(last_guest,)
        for i in range(len(record)):
            total_happiness +=happiness_dict[record[i]][record[i-1]]+happiness_dict[record[i-1]][record[i]]
        optimal_happiness = max(optimal_happiness, total_happiness)
    
    return optimal_happiness

def q13_2015_part2(): 
    input=get_input('13', '2015').splitlines()
    guest_set = set()
    happiness_dict = dict()
    for line in input: #construct data structure
        data = line.split()
        source=data[0]
        dest=data[10].replace('.', '')
        happiness=int(data[3]) if data[2]=='gain' else -int(data[3])
        guest_set.add(source)
        guest_set.add(dest)
        happiness_dict.setdefault(source, dict())[dest] = happiness
    
    optimal_happiness =0
    for record in permutations(guest_set):
        total_happiness = 0
        ##consider host just sit between first and last guest, 
        ##then no need calculate happiness between 1st and last guest
        for i in range(1, len(record)): 
            total_happiness +=happiness_dict[record[i]][record[i-1]]+happiness_dict[record[i-1]][record[i]]
        optimal_happiness = max(optimal_happiness, total_happiness)
    
    return optimal_happiness
##通过运行part1，2得出结论，主人的加入让客人的幸福度降低 -_-!!

####===>  Day 14 Solution <===####    
def q14_2015_part1():
    input=get_input('14', '2015').splitlines()
    total_time=2503
    max_dist=0
    for line in input:
        data=line.split()
        (speed, fly_time, period, period_dist)=(int(data[3]), int(data[6]), 
                                                int(data[6])+int(data[13]), int(data[3])*int(data[6]))
        fly_dist=total_time//period*period_dist + min(total_time%period,fly_time)*speed
        max_dist=max(max_dist, fly_dist)
    return max_dist

def q14_2015_part2():
    input=get_input('14', '2015').splitlines()
    stats_dict={}
    total_time=2503
    for line in input: ##construct each player's statistics
        data=line.split()
        stats_dict[data[0]]={'speed':int(data[3]), 
                            'fly_time':int(data[6]), 
                            'period':int(data[6])+int(data[13]), 
                            'period_dist':int(data[3])*int(data[6]),
                            'score':0}
    
    ##scan each second to score players
    for time_elapsed in range(1, total_time+1):
        max_dist=0
        player_to_score=set()
        for player, stats in stats_dict.items():
            #flying distance by time_elapsed
            fly_dist=time_elapsed//stats['period']*stats['period_dist'] +min(time_elapsed%stats['period'], stats['fly_time'])*stats['speed']
            ##find lead player in this round
            if fly_dist>max_dist:
                player_to_score.clear()
                player_to_score.add(player)
                max_dist=fly_dist
            elif fly_dist==max_dist:
                player_to_score.add(player)
        for player in player_to_score: # score lead player(s)
            stats_dict[player]['score']+=1
    
    max_score=0 #find max score  
    for player, stats in stats_dict.items():
        max_score=max(max_score,  stats['score'])
        
    return max_score

####===>  Day 15 Solution <===####    
def q15_2015_part1():
    input=get_input('15', '2015').splitlines()
    total_unit=100
    ingre_stats=[]
    for line in input:
        #’Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3‘
        data=line.replace(':', '').replace(',', '').split()
        ingre_stats.append({'ingredient':data[0],
                            'capacity':int(data[2]), 
                            'durability':int(data[4]), 
                            'flavor':int(data[6]), 
                            'texture':int(data[8]),
                            'calories':int(data[10]),})
    ## 100汤匙分配给4种配料，相当于在 '1 1 1 1...'(100个)中插入三个隔板
    ## 隔板可以选的位置有99个,组合数 c（3，99）
    max_score=0
    for record in combinations(range(1, total_unit), len(ingre_stats)-1):
        units=[record[0], record[1]-record[0],record[2]-record[1],total_unit-record[2]]
        (capacity, durability, flavor, texture)=(0,0,0,0)
        for index in range(len(ingre_stats)):
            capacity+=ingre_stats[index]['capacity']*units[index]
            durability+=ingre_stats[index]['durability']*units[index]
            flavor+=ingre_stats[index]['flavor']*units[index]
            texture+=ingre_stats[index]['texture']*units[index]
        total_score=max(0,capacity)*max(0,durability)*max(0,flavor)*max(0,texture)
        max_score=max(max_score, total_score)
    
    return max_score

def q15_2015_part2_old():
    input=get_input('15', '2015').splitlines()
    total_unit=100
    ingre_stats=[]
    for line in input:
        #’Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3‘
        data=line.replace(':', '').replace(',', '').split()
        ingre_stats.append({'ingredient':data[0],
                            'capacity':int(data[2]), 
                            'durability':int(data[4]), 
                            'flavor':int(data[6]), 
                            'texture':int(data[8]),
                            'calories':int(data[10]),})
    
    ##更好的方案是先找出所有让calories=500的组合，然后找出其中的highest-scoring
    ##这样可以排除绝大多数组合，提高运行效率，有时间可以试下
    max_score=0
    for record in combinations(range(1, total_unit), len(ingre_stats)-1):
        units=[record[0], record[1]-record[0],record[2]-record[1],total_unit-record[2]]
        (capacity, durability, flavor, texture, calories)=(0,0,0,0, 0)
        for index in range(len(ingre_stats)):
            capacity+=ingre_stats[index]['capacity']*units[index]
            durability+=ingre_stats[index]['durability']*units[index]
            flavor+=ingre_stats[index]['flavor']*units[index]
            texture+=ingre_stats[index]['texture']*units[index]
            calories+=ingre_stats[index]['calories']*units[index]
        if calories!=500:
            continue
        total_score=max(0,capacity)*max(0,durability)*max(0,flavor)*max(0,texture)
        max_score=max(max_score, total_score)
    
    return max_score 
      
##alternative improved solution for q15 part2 
def q15_2015_part2():
    input=get_input('15', '2015').splitlines()
    total_unit=100
    ingre_stats=[]
    for line in input:
        #’Sprinkles: capacity 2, durability 0, flavor -2, texture 0, calories 3‘
        data=line.replace(':', '').replace(',', '').split()
        ingre_stats.append({'ingredient':data[0],
                            'capacity':int(data[2]), 
                            'durability':int(data[4]), 
                            'flavor':int(data[6]), 
                            'texture':int(data[8]),
                            'calories':int(data[10]),})
    
    ##找出所有让calories=500的组合，然后找出其中的highest-scoring
    ##这样可以排除绝大多数组合，提高运行效率，有时间可以试下
    max_score=0
    for i in range(1, 500//ingre_stats[0]['calories']+1):
        for j in range(1, (500-ingre_stats[0]['calories']*i)//ingre_stats[1]['calories']+1):
            for k in range(1, (500-ingre_stats[0]['calories']*i-ingre_stats[1]['calories']*j)//ingre_stats[2]['calories']+1):
                remaining_cal=500-ingre_stats[0]['calories']*i-ingre_stats[1]['calories']*j-ingre_stats[2]['calories']*k
                n=remaining_cal//ingre_stats[3]['calories']
                if remaining_cal%ingre_stats[3]['calories']==0 and i+j+k+n==total_unit: 
                    (capacity, durability, flavor, texture, calories)=(0,0,0,0,0)
                    units=[i, j, k, n]
                    for index in range(len(ingre_stats)):
                        capacity+=ingre_stats[index]['capacity']*units[index]
                        durability+=ingre_stats[index]['durability']*units[index]
                        flavor+=ingre_stats[index]['flavor']*units[index]
                        texture+=ingre_stats[index]['texture']*units[index]
                    total_score=max(0,capacity)*max(0,durability)*max(0,flavor)*max(0,texture)
                    max_score=max(max_score, total_score)                   
    
    return max_score   

####===>  Day 16 Solution <===####    
def q16_2015_part1():
    input=get_input('16', '2015').splitlines()
    msg={'children': '3', 'cats': '7', 'samoyeds': '2', 'pomeranians': '3', 'akitas': '0', 
         'vizslas': '0', 'goldfish': '5', 'trees': '3', 'cars': '2', 'perfumes': '1'}    
    for line in input:
        data=line.replace(':','').replace(',','').split()
        sue_info={data[2]:data[3], data[4]:data[5], data[6]:data[7]}
        #find items in common, only if 3 common items, then must be the Aunt Sue
        if len(msg.items() & sue_info.items())==3:
            return data[1]

def q16_2015_part2():
    input=get_input('16', '2015').splitlines()
    #append '>' or '<' to ranges value
    msg={'children': '3', 'cats': '>7', 'samoyeds': '2', 'pomeranians': '<3', 'akitas': '0', 
         'vizslas': '0', 'goldfish': '<5', 'trees': '>3', 'cars': '2', 'perfumes': '1'}    
    for line in input:
        data=line.replace(':','').replace(',','').split()
        ## update value matched items to same value as in msg for cats/trees/pomeranians/goldfish
        for i in [2, 4, 6]:
            if data[i]=='cats' and int(data[i+1])>7: data[i+1]='>7'
            elif data[i]=='trees' and int(data[i+1])>3: data[i+1]='>3'
            elif data[i]=='pomeranians' and int(data[i+1])<3: data[i+1]='<3'
            elif data[i]=='goldfish' and int(data[i+1])<5: data[i+1]='<5'
        sue_info={data[2]:data[3], data[4]:data[5], data[6]:data[7]}
        ##find items in common, only if 3 common items, then must be the Aunt Sue
        if len(msg.items() & sue_info.items())==3:
            return data[1]
 
####===>  Day 17 Solution <===####      
def q17_2015_part1():
    input=get_input('17', '2015').splitlines()
    total_liter=150
    containers=[]
    for line in input:
       containers.append(int(line)) 
    containers.sort()
    return find_solution(containers, total_liter)            
##recursively divide the problem into 1)with the first container involved 2)without the first container involved
##list must be sorted for this solution to work          
def find_solution(list, liter):
    if not list or liter<list[0]:
        return 0
    elif liter==list[0]:
        return 1+find_solution(list[1:],liter)    
    return find_solution(list[1:],liter)+find_solution(list[1:],liter-list[0])

def q17_2015_part2():
    input=get_input('17', '2015').splitlines()
    total_liter=150
    counter=0
    containers=[]
    for line in input:
       containers.append(int(line)) 
    containers.sort()
    ##search combination from the possible minimum: total_liter//containers[-1]+1
    for n in range(total_liter//containers[-1]+1, total_liter//containers[0]+1):
        for c in combinations(containers, n):
            if sum(c)== total_liter:
                counter+=1
        if counter>0:
            return counter      

####===>  Day 18 Solution <===####
def q18_2015_part1():
    return q18_2015(total_steps=100, part=1)

def q18_2015_part2():
    return q18_2015(total_steps=100, part=2)
    
def q18_2015(total_steps=100, part=1): #shared by part1 and part2
    '''
        A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
        A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
    '''
    input=get_input('18', '2015').splitlines()
    ##surround the 100*100 matrix by circle of 0, then 102*102
    ##then no light will be at the edge and outside extra 0 won't affect the calculation
    light_matrix=[[0 for i in range(len(input)+2)]]
    for line in input:
        line='0'+line.replace('#','1').replace('.','0')+'0'
        light_matrix.append(list(map(int, list(line))))
    light_matrix.append([0 for i in range(len(input)+2)])   
    ##find status for next step
    for i in range(total_steps):
        if part==2:
            (light_matrix[1][1], light_matrix[1][-2], light_matrix[-2][1], light_matrix[-2][-2])=(1,1,1,1)
        light_matrix=next_step(light_matrix)
    if part==2:
        (light_matrix[1][1], light_matrix[1][-2], light_matrix[-2][1], light_matrix[-2][-2])=(1,1,1,1)
    ## find total count of light on
    total_on=0
    for i in range(len(light_matrix)):
        total_on+=sum(light_matrix[i])
    return total_on
            
def next_step(orin_matrix):
    # make sure clone each element rather than only 1st-layer child
    new_matrix=copy.deepcopy(orin_matrix)
    for i in range(1, len(orin_matrix)-1):
        for j in range(1, len(orin_matrix[i])-1):
            neighbors_on=sum(orin_matrix[i-1][j-1:j+2])+sum(orin_matrix[i+1][j-1:j+2])+orin_matrix[i][j-1]+orin_matrix[i][j+1]
            if neighbors_on==3:
                new_matrix[i][j]=1
            elif orin_matrix[i][j]==1 and neighbors_on!=2:
                new_matrix[i][j]=0
    return new_matrix

####===>  Day 19 Solution <===####      
def q19_2015_part1():
    input =get_input('19', '2015').splitlines()
    molecule_set=set()
    molecule=input[-1]
    for line in input[:-2]:
        (to_find, _, replacement)=line.split()
        create_molecule(to_find, replacement, molecule, molecule_set)
    return len(molecule_set)

def create_molecule(to_find, replacement, molecule, molecule_set):
    for match in re.finditer(to_find, molecule):
        #split string into 2 by match position, replace the first match in second string, then merge
        position=match.start()
        first_part = molecule[:position]
        second_part = molecule[position:]
        second_part = second_part.replace(to_find, replacement, 1)
        molecule_set.add( first_part + second_part) 
       
def q19_2015_part2():
    input =get_input('19', '2015').splitlines() 
    rep={}  # to store all replacement map
    ## after observation by find_pattern() and replacement dictionary, pattern *Rn***Ar can only be produced 
    ## from replacement dictionary which is not dividable anymore. all following logic is based on this
    special_rep={} # to store Rn***Ar pattern map
    (line, molecule)=(input[0], input[-1])
    molecule_set={molecule}
    for line in input[:-2]:
        replacement=line.replace('=>', '').split()
        if 'Ar' in replacement[1]:
            special_rep[replacement[1]]=replacement[0]
        rep[replacement[1]]=replacement[0]
        
    ## to store all 2-step achievable map for special_rep. e.g. Al => ThRnFAr => ThCaRnFAr
    ## this is very useful for quick reference of replacement in replace_with_rep
    rep_2step={} 
    for k, v in special_rep.items():
        for k1, v1 in rep.items():
            if v1 in k.split('R')[0]:
                rep_2step[k.split('R')[0].replace(v1, k1)+'R'+k.split('R')[1]]=v
    
    replacements={'special_rep':special_rep, 'rep':rep, 'rep_2step':rep_2step,}
    
    step_counter=[0,] #need pass to function by reference
    while True:
        #find the first matched to above, start with 'R' end with 'r', Rn***Ar
        molecule=replace_with_rep(molecule, replacements, step_counter)
        if 'r' not in molecule: #once no Rn***Ar pattern, just replace until get 'e'
            molecule=replace_with_rep(molecule, replacements, step_counter, 0, len(molecule))
            return step_counter[0]
        end_pos  =molecule.index('r')
        start_pos =molecule[:end_pos].rfind('R')
        molecule=replace_with_rep(molecule, replacements, step_counter, start_pos, end_pos) 
          
##replace specific range of molecule with replacements dictionary
def replace_with_rep(molecule, replacements, step_counter, start_pos=-1, end_pos=0):
    m_before=''
    if start_pos==-1: # for whole molecule replacement
        m_after=molecule 
        rep=replacements['special_rep']
    else: # replacement for only special pattern
        m_after= molecule[start_pos:end_pos+1]
        rep=replacements['rep']
    while m_before!=m_after:
        m_before=m_after
        for k, v in rep.items():
            if k in m_after:
                step_counter[0]+=m_after.count(k)
                m_after=m_after.replace(k, v)
                
    if start_pos!=-1:
        #while m_after not in replacements['special_rep']:
        for k, v in replacements['rep_2step'].items():
            to_match=molecule[max(0,start_pos-15):start_pos]+m_after
            if k in to_match:
                to_match=to_match.replace(k, v)
                step_counter[0]+=2
                return molecule[:max(0,start_pos-15)]+to_match+molecule[end_pos+1:]
        m_after=molecule[:start_pos]+m_after+molecule[end_pos+1:]
    return m_after
## all patterns starts with *Rn and end with Ar 
def find_pattern(rep):
    s=set()
    for k in rep.keys():
        for v in rep.values():      
            if v in k:
                k=k.replace(v, '*')
        if k != len(k) * '*': 
            s.add(k)
    #print(s)                     

####===>  Day 20 Solution <===####  
def q20_2015_part1():
    input=int(get_input('20', '2015')) #29000000
    ##if house number =n!, then this house will get more presents then any house < n.could easy prove
    ## use this to estimate lower and up bound of solution     
    n=house=1
    while presents_number(factorial(n))<input:
        n+=1
    house=factorial(n-1)
    while presents_number(house)<input:
        house+=1    
    return house          
def presents_number(n):    #to get total presents of nth house
    total, squrt, flr_sqrt=0, n**0.5, int(n**0.5)    
    for i in range(1, flr_sqrt+1 ):
         if n % i == 0:
             total+=i+n//i
    if flr_sqrt==squrt:
        total-=flr_sqrt
    return total*10

##tried approach in part1 which run very long as divide operation is high cost
##try iterate elf and its delivered presents to each house then find the answer
def q20_2015_part2():
    input=int(get_input('20', '2015')) #29000000
    ##house n get at lease 11*n presents hence upper bound is input/11. can narrow down further by trying 2^n
    ## as exist 50 delivery constraint, answer for part2 must be bigger than part1
    ## so part1_answer can be used as lower bound. also part1_answer/50 is lower bound for elf
    part1_answer=665280 
    max=int(input/11) 
    presents=[0]*max
    for elf in range(int(part1_answer/50), max):  #iteration from 1st elf to max
        count=0
        for house in range(elf, max, elf): #nth elf delivers to house n, 2n, 3n.. present 11n until count to 50
            count+=1
            presents[house]+=elf*11
            if count==50:break
    
    for house in range(665280, max): #search the answer
        if presents[house]>=input: return house
        
 ## part1 use less memory but more time. vice versa for part2 ##   
 
 ####===>  Day 21 Solution <===#### 
def q21_2015_part1():
    return q21_2015()[0]

def q21_2015_part2():
    return q21_2015()[1]

def q21_2015(): # shared by part 1 and 2
    
    boss={'points': 109, 'damage': 8,'armor': 2,} # boss property
    player={'points':100, 'damage': 0,'armor': 0,} # player property
    weapons={4:8, 5:10, 6:25, 7:40, 8:74,}  # weapons dict in damage:cost form
    armors={0:0, 1:13, 2:31, 3:53, 4:75, 5:102,} # armors dict in armor:cost form
    damage_rings={0:0, 1:25, 2:50, 3:100,} #damage ring in damage:cost form
    damage_2rings={ 3:75, 4:125, 5:150,} #case for player choose 2 damage ring
    defense_rings={0:0, 1:20, 2:40, 3:80,} #defense ring in armor:cost form
    defense_2rings={3:60, 4:100, 5:120,} #case for player choose 2 defense ring
    least_gold, max_gold=100000, 0
    ##just try all combinations
    for w, wd in weapons.items():
        for a, ad in armors.items():
            for dm_r, dm in damage_rings.items(): # case of 0 or 1 ring
                for df_r, df in defense_rings.items():
                    player['damage']=w+dm_r
                    player['armor']=a+df_r
                    gold_spend=wd+ad+dm+df
                    if is_win(player, boss):
                        least_gold=min(gold_spend, least_gold)
                    else: max_gold=max(gold_spend, max_gold)
            for dm_2r, dm2 in damage_2rings.items(): #case of 2 damage ring
                player['damage']=w+dm_2r
                player['armor']=a
                gold_spend=wd+ad+dm2
                if is_win(player, boss):
                    least_gold=min(gold_spend, least_gold)
                else: max_gold=max(gold_spend, max_gold)
            for df_2r, df2 in defense_2rings.items():  #case of 2 defense ring
                player['damage']=w
                player['armor']=a+df2
                gold_spend=wd+ad+dm2
                if is_win(player, boss):                    
                    least_gold=min(gold_spend, least_gold)
                else: max_gold=max(gold_spend, max_gold)   
    return least_gold, max_gold

def is_win(player, boss): #check if play wins
    boss_down=ceil(boss['points']/max(1, (player['damage']-boss['armor'])))
    player_down=ceil(player['points']/max(1,(boss['damage']-player['armor'])))
    return True if player_down>=boss_down else False

 ####===>  Day 22 Solution <===####
def q22_2015_part1():
    return q22_2015(part=1)

def q22_2015_part2():
    return q22_2015(part=2)
 
def q22_2015(part=1):  #shared by part1 and 2, just comment/uncomment first line player_turn() for part 1 or 2 solution
    ##construct data structure, spells: static data, state: real time data
    spells={   'm_m':  {'cost':53,  'damage':4, },
              'drain': {'cost':73,  'damage':2, 'heal': 2}, 
            'shield':  {'cost':113, 'turn':6,   'armor':7},
            'poison':  {'cost':173, 'turn':6,   'damage':3},
            'recharge':{'cost':229, 'turn':5,   'mana': 101}}           
    state={'player': {'points':50, 'mana': 500, 'armor':0}, 
           'boss': {'points': 71 }, 
           'effect': {'shield':0, 'poison':0, 'recharge':0, },
           'spend':0}    
    min_spend=[100000] # any big number for initial mana, use object not value for function pass  
    ##recursively take turns between player and boss until one party lose
    player_turn(state, spells, min_spend, part)
    return min_spend[0]
def player_turn(state, spells, min_spend, part):
    if part==2: state['player']['points']-=1  #!!!uncomment this line for part 2
    ## update state with remaining effect: shield, poison, recharge
    if state['effect']['shield']: #update shield if exist
        state['effect']['shield']=state['effect']['shield']-1
        if not state['effect']['shield']: 
            state['player']['armor']=0
    if state['effect']['poison']: #update poison if exist
        state['boss']['points']-=spells['poison']['damage']
        if state['boss']['points']<=0: 
            min_spend[0]=min(min_spend[0], state['spend'])
            # print('boss down', min_spend[0])
            return
        state['effect']['poison']-=1
    if state['effect']['recharge']: #update recharge if exist
        state['player']['mana']+=spells['recharge']['mana']
        state['effect']['recharge']-=1
    ## starting of player cast ##
    ## case: cast Magic Missile ##
    if state['player']['mana']>=spells['m_m']['cost']:
        state_mm=copy.deepcopy(state)
        state_mm['player']['mana']-=spells['m_m']['cost']
        state_mm['boss']['points']-=spells['m_m']['damage']
        state_mm['spend']+=spells['m_m']['cost']
        if state_mm['boss']['points']<=0: 
            min_spend[0]=min(min_spend[0], state_mm['spend'])
            # print('boss down', min_spend[0])
            return
        boss_turn(state_mm, spells, min_spend, part)
    #if not enough mana
    elif state['effect']['recharge']: boss_turn(state, spells, min_spend, part)
    else: return 
    ## case: cast drain ##
    if state['player']['mana']>=spells['drain']['cost']:
        state_drain=copy.deepcopy(state)
        state_drain['player']['mana']-=spells['drain']['cost']
        state_drain['player']['points']+=spells['drain']['heal']
        state_drain['boss']['points']-=spells['drain']['damage']
        state_drain['spend']+=spells['drain']['cost']
        if state_drain['boss']['points']<=0: 
            min_spend[0]=min(min_spend[0], state_drain['spend'])
            # print('boss down', min_spend[0])
            return
        boss_turn(state_drain, spells, min_spend, part) 
    ## case: cast shield ##      
    if not state['effect']['shield'] and state['player']['mana']>=spells['shield']['cost']:
        state_shield=copy.deepcopy(state)
        state_shield['player']['mana']-=spells['shield']['cost']
        state_shield['player']['armor']=spells['shield']['armor']
        state_shield['effect']['shield']=spells['shield']['turn']
        state_shield['spend']+=spells['shield']['cost']
        boss_turn(state_shield, spells, min_spend, part) 
    ## case: cast poison ##  
    if not state['effect']['poison'] and state['player']['mana']>=spells['poison']['cost']:
        state_poison=copy.deepcopy(state)
        state_poison['player']['mana']-=spells['poison']['cost']
        state_poison['effect']['poison']=spells['poison']['turn']
        state_poison['spend']+=spells['poison']['cost']
        boss_turn(state_poison, spells, min_spend, part)
     ## case: cast recharge ## 
    if not state['effect']['recharge'] and state['player']['mana']>=spells['recharge']['cost']:
        state_recharge=copy.deepcopy(state)
        state_recharge['player']['mana']-=spells['recharge']['cost']
        state_recharge['effect']['recharge']=spells['recharge']['turn']
        state_recharge['spend']+=spells['recharge']['cost']
        boss_turn(state_recharge, spells, min_spend, part) 
def boss_turn(state, spells, min_spend, part):
    ## update state with remaining effect: shield, poison, recharge
    if state['effect']['shield']: #update shield if exist
        state['effect']['shield']=state['effect']['shield']-1
        if not state['effect']['shield']: 
            state['player']['armor']=0
    if state['effect']['poison']: #update poison if exist
        state['boss']['points']-=spells['poison']['damage']
        if state['boss']['points']<=0: 
            min_spend[0]=min(min_spend[0], state['spend'])
            return
        state['effect']['poison']-=1
    if state['effect']['recharge']: #update recharge if exist
        state['player']['mana']+=spells['recharge']['mana']
        state['effect']['recharge']-=1
    
    state['player']['points']-=(10- state['player']['armor'])
    if state['player']['points']<=0: # player lose
        return
    player_turn(state, spells, min_spend, part)  
    
####===>  Day 23 Solution <===####
def q23_2015_part1():
    return q23_2015(a=0)

def q23_2015_part2():
    return q23_2015(a=1)
  
def q23_2015(a=0):
    input=get_input('23', '2015').replace(',', '').splitlines()
    b, pointer=0, 0  
    
    ## just translate the instruction and run until out of bound
    ## alternatively, could use exec() function which is faster for parse string to code
    ## e.g. exec('b+=1') >> b=1
    while True:
        ins= input[pointer].split()
        if ins[0] == 'hlf':
            if ins[1]=='a': a=int(a/2)
            else: b=int(b/2)
            pointer+=1
            
        elif ins[0] == 'tpl':
            if ins[1]=='a': a=3*a
            else: b=3*b
            pointer+=1
        
        elif ins[0] == 'inc':
            if ins[1]=='a': a+=1
            else: b+=1
            pointer+=1
            
        elif ins[0] == 'jmp':
            pointer+=int(ins[1])
            
        elif ins[0] == 'jie':
            if ins[1]=='a' and a%2==0: pointer+=int(ins[2])
            elif ins[1]=='b' and b%2==0: pointer+=int(ins[2])
            else: pointer+=1
            
        elif ins[0] == 'jio':
            if ins[1]=='a' and a==1: pointer+=int(ins[2])
            elif ins[1]=='b' and b==1: pointer+=int(ins[2])
            else: pointer+=1
        if pointer>=len(input) or pointer<0:
            break
    
    return b   

####===>  Day 24 Solution <===#### 
def q24_2015_part1():
    return q24_2015(groups=3) 

def q24_2015_part2():
    return q24_2015(groups=4) 
 
def q24_2015(groups=3):
    input=get_input('24', '2015').splitlines()
    packs=[]
    for pack in input:
        packs.append(int(pack))
    required=int(sum(packs)/groups)
    comb=[] #group of packs for one solution
    result=[[0]*30,] # to store solution with least packs 
    packs.sort()
    result = find_fit(packs, required, comb, result) 
    best_qe=10**15 #any big number
    for record in result: #find best qe
        qe=numpy.prod(record)   
        best_qe=min(best_qe, qe)
    return best_qe   
##very similar to q17       
def find_fit(packs, required, comb, result):
    if not packs or required<packs[0]:
        return False #no solution
    elif required==packs[0]: # solution found and check if it has least packs comparing to existing
        comb.append(packs[0])
        if len(comb)<len(result[0]):
            result.clear()
            result.append(comb)
        elif len(comb)==len(result[0]):
            result.append(comb)
        return True
    comb1=comb.copy()
    comb1.append(packs[0]) 
    find_fit(packs[1:],required, comb, result) # with first pack not involved
    find_fit(packs[1:],required-packs[0], comb1, result) # with first pack involved                   
    return result 

####===>  Day 25 Solution <===####
##codes paper是一个斜放的三角形，(row, column) 对应的数字应该为 (n-1)*(n-2)/2+column where n=row+column, 等差数列求和
def q25_2015_part1():
    required =(3010, 3019) #my input
    index= (sum(required)-1)*(sum(required)-2)//2+required[1]
    a=20151125 #inital number
    
    for i in range(1, index):
        a=(a*252533)%33554393   
    return a 

def q25_2015_part2():
    return 'All done for 25 days'

     
###########  Execution  ############# 
# start_time=time.time()+1.2  #realized get_input() costs roughly 1.2s which should not be counted for execution
# result=q25_2015_part1()
# end_time=time.time()
# print('result:',result ,'|| execution time: %s s'%"{:.2f}".format(end_time-start_time))

