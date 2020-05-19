import requests
from pycookiecheat import chrome_cookies #pip3 install pycookiecheat
import hashlib 
import re
import time
import json
from tsp_solver.greedy import solve_tsp #pip3 install tsp_solver2
from itertools import permutations, combinations

###########  Global Function  #############

#To retrieve question input with param: year and question number
#To invoke this function, login onto Github with chrome is a must 
def get_input(question_num, year='2015'):
    input_url='https://adventofcode.com/'+year+'/day/'+question_num+'/input'
    cookies = chrome_cookies(input_url)    
    content = requests.get(input_url, cookies=cookies).text
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
            print(str_to_check)
            
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
    print('get_signal for ', destination)
    if destination.isnumeric(): # case: 123 
        return int(destination)
    
    instruction=circuit_dict[destination].split()
    print(circuit_dict[destination],'-->', destination)
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
def q10_2015(repeat_count): 
    input='1113122113'
    re_digit = re.compile(r'((\d)\2*)') #find repeated digit
    for i in range(repeat_count):
        print('loop', i)
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
def q15_2015_part2_2():
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
    
###########  Execution  #############
start_time=time.time()
result=q16_2015_part2()
end_time=time.time()
print('result:',result ,'|| execution time: %s s'%"{:.2f}".format(end_time-start_time))

