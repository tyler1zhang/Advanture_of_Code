# -*- coding: utf-8 -*-
import re
import time
from itertools import permutations, combinations, cycle
from math import factorial, ceil
from collections import Counter, OrderedDict
import hashlib 
import copy
from collections import deque

###########  Global Function  #############

#To retrieve question input with param: year and question number
#To invoke this function, login onto Github with chrome is a must 
def get_input(question_num, year='2016'):
    f = open("input/q%s_2016.txt"%question_num, "r")
    content=f.read()
    f.close()
    return content

###########  Starting of Solution  #############

####===>  Day 1 Solution <===####
def q1_2016_part1():
    input=get_input('1', 2016)
    direction=0  # 0-north, 1-east,  2-south, 3-west
    position=[0, 0]
    seq=input.replace(',', '').split()
    for ins in seq:
        direction=(direction+ (1 if ins[0]=='R' else -1))%4
        if direction==0:
            position[1]+=int(ins[1:])
        elif direction==2:
            position[1]-=int(ins[1:])
        elif direction==1:
            position[0]+=int(ins[1:])
        else: position[0]-=int(ins[1:])
    return abs(position[1])+abs(position[0])

def q1_2016_part2():
    input=get_input('1', 2016)
    direction=0  # 0-north, 1-east,  2-south, 3-west
    position=[0, 0]
    position_set=set()
    seq=input.replace(',', '').split()
    for ins in seq:
        direction=(direction+ (1 if ins[0]=='R' else -1))%4
        if direction==0:
            for i in range(1, int(ins[1:])+1):
                if (position[0], position[1]+ i ) in position_set:
                    return abs(position[1]+ i)+abs(position[0])
                position_set.add((position[0], position[1]+ i ))
            position[1]+=int(ins[1:])
        elif direction==2:
            for i in range(1, int(ins[1:])+1):
                if (position[0], position[1]-i ) in position_set:
                    return abs(position[1]- i)+abs(position[0])
                position_set.add((position[0], position[1]- i ))
            position[1]-=int(ins[1:])
        elif direction==1:
            for i in range(1, int(ins[1:])+1):
                if (position[0]+ i, position[1] ) in position_set:
                    return abs(position[1])+abs(position[0]+ i)
                position_set.add((position[0]+ i, position[1] ))
            position[0]+=int(ins[1:])
        else:
            for i in range(1, int(ins[1:])+1):
                if (position[0]- i, position[1] ) in position_set:
                    return abs(position[1])+abs(position[0]-i)
                position_set.add((position[0]-i, position[1] )) 
            position[0]-=int(ins[1:])

####===>  Day 2 Solution <===####
def q2_2016_part1():
    input=get_input('2', '2016').splitlines()
    keypad=[[1,2,3],
            [4,5,6],
            [7,8,9]]
    x, y=1, 1
    code=[]
    for ins in input:
        for char in ins:
            if char=='L':
                y=max(y-1, 0)
            elif char=='R':
                y=min(y+1, 2)
            elif char=='D':
                x=min(x+1, 2)
            elif char=='U':
                x=max(x-1, 0)
        code.append(keypad[x][y])
    return (code)

def q2_2016_part2():
    input=get_input('2', '2016').splitlines()
    keypad=[    [0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0],
                [0,0,2,3,4,0,0],
                [0,5,6,7,8,9,0],
            [0,0,'A','B','C',0,0],
               [0,0,0,'D',0,0,0],
               [0,0,0,0,0,0,0]]
    x, y=3, 1
    code=[]
    for ins in input:
        for char in ins:
            if char=='L' and keypad[x][y-1]:
                y-=1
            elif char=='R' and keypad[x][y+1]:
                y+=1
            elif char=='D' and keypad[x+1][y]:
                x+=1
            elif char=='U' and keypad[x-1][y]:
                x-=1
        code.append(keypad[x][y])
    return (code)
 
####===>  Day 3 Solution <===####
def q3_2016_part1():
    input=get_input('3', '2016').splitlines()
    count=0
    for line in input:
        data= line.split()
        a, b, c=int(data[0]), int(data[1]),int(data[2]), 
        if a+b>c and a+c>b and b+c>a: count+=1
    return count 

def q3_2016_part2():
    input=get_input('3', '2016').splitlines()
    count=0
    for i in range(0, len(input), 3):
        data=[]
        for j in range(3):
            data.append(input[i+j].split())
        for j in range(3):
            a, b, c=int(data[0][j]), int(data[1][j]),int(data[2][j]), 
            if a+b>c and a+c>b and b+c>a: count+=1
    return count

####===>  Day 4 Solution <===####
def q4_2016_part1():
    input=get_input('4', '2016').splitlines()
    total=0
    for room in input:
        [letters, tail]=room.rsplit('-',1)
        [id, checksum, _]=re.split('\[|\]', tail)
        counter = Counter(letters.replace('-', ''))
        counter=sorted(counter.items(), key=lambda x: (-x[1],x[0]))
        check=''
        for i in range(5):
            check+=counter[i][0]
        if check==checksum:
            total+=int(id)
    return total

def q4_2016_part2():
    input=get_input('4', '2016').splitlines()
    total=0
    index_z=ord('z')
    for room in input:
        [code, id]=room.split('[')[0].rsplit('-', 1)
        incr=int(id)%26
        word=code.replace('-', ' ')
        match='northpole object'
        for i in range(len(match)):
            char=word[i]
            if char==' ' and match[i]==' ': continue
            index=ord(char)
            index= index+incr if index+incr<=index_z else index+incr-26
            char=chr(index)
            if char!=match[i]: break
            if i==len(match)-1:return id
            

####===>  Day 5 Solution <===####
def q5_2016_part1():
    input=get_input('5', '2016').splitlines()[0]
    suffix=0
    str_to_match='00000'
    pw=''
    while True: #Exhaustive search until find the match
        secret_key=input+str(suffix)
        hash = hashlib.md5(secret_key.encode()).hexdigest()
        if hash[:5]==str_to_match:
            pw+= hash[5]
            if len(pw)==8: break
        suffix+=1
    return pw

def q5_2016_part2():
    input=get_input('5', '2016').splitlines()[0]
    suffix=0
    str_to_match='00000'
    pw='********'
    pos=[str(i) for i in range(8)]
    while True: #Exhaustive search until find the match
        secret_key=input+str(suffix)
        hash = hashlib.md5(secret_key.encode()).hexdigest()
        if hash[:5]==str_to_match and hash[5] in pos:
            if pw[int(hash[5])]=='*': pw=pw[:int(hash[5])]+hash[6]+pw[int(hash[5])+1:]
            if '*' not in pw:  return pw
        suffix+=1

####===>  Day 6 Solution <===####
def q6_2016_part1():
    return q6_2016(1)
    
def q6_2016_part2():
    return q6_2016(2)

def q6_2016(part=1):
    input =get_input('6', '2016').splitlines()
    cols=['']*len(input[0])
    msg=''
    for line in input:
        for i in range(len(cols)):
            cols[i]+=line[i]
    for col in cols:
        msg+=Counter(col).most_common()[0 if part==1 else -1][0]
    return msg
 
####===>  Day 7 Solution <===####
def q7_2016_part1():
    input=get_input('7', '2016').splitlines()
    ip_count=0
    for line in input:
        strs=re.split('\[|\]', line)
        find_abba_out=False
        no_abba_in=True
        for i in range(0, len(strs), 2):
            str=strs[i]
            is_abba= any(a1==a4 and b2==b3 and a1!=b2 for a1, b2, b3, a4 in zip(str, str[1:], str[2:], str[3:]))
            if is_abba:
                find_abba_out=True
                break
        for i in range(1, len(strs), 2):
            str=strs[i]
            is_abba= any(a1==a4 and b2==b3 and a1!=b2 for a1, b2, b3, a4 in zip(str, str[1:], str[2:], str[3:]))
            if is_abba:
                no_abba_in=False
                break
        if find_abba_out and no_abba_in:
            ip_count+=1
            
    return  ip_count       

def q7_2016_part2():
    input=get_input('7', '2016').splitlines()
    ip_count=0
    for line in input:
        strs=re.split('\[|\]', line)
        aba_set=set()
        no_abba_in=True
        for i in range(0, len(strs), 2):
            str=strs[i]
            for a1, b2, a3 in zip(str, str[1:], str[2:]):
                if a1==a3 and a1!=b2:
                    aba_set.add(a1+b2+a3)
        for i in range(1, len(strs), 2):
            str=strs[i]
            for a1, b2, a3 in zip(str, str[1:], str[2:]):
                if a1==a3 and a1!=b2 and b2+a1+b2 in aba_set:
                    ip_count+=1
                    break
            
    return  ip_count  

####===>  Day 8 Solution <===####
def q8_2016_part1():
    input=get_input('8', '2016').splitlines()
    
    screen=[[0 for i in range(50)] for k in range(6)]
    for ins in input:
        if 'rect' in ins:
            [x, y]=ins.split()[1].split('x')
            rect(int(y), int(x), screen)
        elif 'rotate row' in ins:
            [a, shift]=ins.split('=')[1].split(' by ') 
            rotate_row(int(a), int(shift), screen)
        else:
            [a, shift]=ins.split('=')[1].split(' by ') 
            rotate_col(int(a), int(shift), screen)
    lit_count=0
    for row in screen:
        lit_count+=sum(row)
    
    return lit_count

def q8_2016_part2():
    input=get_input('8', '2016').splitlines()
    
    screen=[[0 for i in range(50)] for k in range(6)]
    for ins in input:
        if 'rect' in ins:
            [x, y]=ins.split()[1].split('x')
            rect(int(y), int(x), screen)
        elif 'rotate row' in ins:
            [a, shift]=ins.split('=')[1].split(' by ') 
            rotate_row(int(a), int(shift), screen)
        else:
            [a, shift]=ins.split('=')[1].split(' by ') 
            rotate_col(int(a), int(shift), screen)
    
def rect(y, x, screen):
    for i in range(y):
        for k in range(x):
            screen[i][k]=1
            
def rotate_row(y, shift, screen):
    row=screen[y].copy()
    screen[y][shift:]=row[:-shift]
    screen[y][:shift]=row[-shift:]
    
def rotate_col(x, shift, screen):
    orin_screen=copy.deepcopy(screen)
    for y in range(len(screen)):
        screen[y][x]=orin_screen[y-shift][x]


####===>  Day 9 Solution <===####
def q9_2016_part1():
    input=get_input('9', '2016').rstrip()
    deco_len=len(input)
    start=input.find('(')
    while start!=-1:
        end=input.find(')', start)
        marker=input[start+1:end]
        [a, b]=marker.split('x')
        deco_len+=(int(a)*(int(b)-1)-len(marker)-2)
        input=input[end+int(a)+1:] #cut off all sub-string current marker covers
        start=input.find('(')
    return deco_len

def q9_2016_part2():
    input=get_input('9', '2016').rstrip()
    return get_deco_len(input)
##recursively divide problem into 3 parts: pure string + (marker and its string) + remaining
def get_deco_len(string):
    start=string.find('(')
    if start==-1:
        return len(string)
    end=string.find(')', start)
    marker=string[start+1:end]
    [a, b]=marker.split('x')
    a, b=int(a), int(b)
    return start+ b*get_deco_len(string[end+1:end+1+a])+get_deco_len(string[end+1+a:])

####===>  Day 10 Solution <===####
def q10_2016_part1():
    input=get_input('10', '2016').splitlines()
    act_bot, resp_bot, states, ins='', [],  {}, {}, 
    for line in input:
        if line.startswith('value'): # value 23 goes to bot 208
            data=line.split()
            value, bot= data[1], data[-2]+' '+data[-1]
            if bot in states:
                states[bot].append(int(value))
                act_bot=bot
            else: states[bot]=[int(value)]       
        else: # bot 125 gives low to bot 58 and high to bot 57
            data=line.split()
            bot, low, high= data[0]+' '+data[1], data[5]+' '+data[6], data[-2]+' '+data[-1]
            ins[bot]=[low, high]
    next_state(act_bot, states, ins, resp_bot)    
    return resp_bot[0]

def q10_2016_part2():
    input=get_input('10', '2016').splitlines()
    act_bot, resp_bot, states, ins='', [],  {}, {}, 
    for line in input: ##build data structure
        if line.startswith('value'): # value 23 goes to bot 208
            data=line.split()
            value, bot= data[1], data[-2]+' '+data[-1]
            if bot in states:
                states[bot].append(int(value))
                act_bot=bot
            else: states[bot]=[int(value)]       
        else: # bot 125 gives low to bot 58 and high to bot 57
            data=line.split()
            bot, low, high= data[0]+' '+data[1], data[5]+' '+data[6], data[-2]+' '+data[-1]
            ins[bot]=[low, high]    
    next_state(act_bot, states, ins, resp_bot)
    return states['output 0'][0]*states['output 1'][0]*states['output 2'][0]
    
def next_state(act_bot, states, ins, resp_bot):
    chips=sorted(states[act_bot])
    for i in range(len(ins[act_bot])):
        bot=ins[act_bot][i]    
        if bot in states:                
            states[bot].append(chips[i])
            states[act_bot].remove(chips[i])
            if 17 in states[bot] and 61 in states[bot]:
                resp_bot.append( bot)
            next_state(bot, states, ins, resp_bot)
        else:
            states[bot]=[chips[i]]
            states[act_bot].remove(chips[i]) 
            
####===>  Day 11 Solution <===####
def q11_2016_part1():
    input=get_input('11', '2016').splitlines()
    index, steps, total_item=0, 0, 0
    ## state[0]: current floor; state[n]: nth floor's Generator and Chips
    intial_state = [1, [0, 0], [0, 0], [0, 0], [0, 0]]
    for line in input: ## read input to initialize the state
        index+=1
        intial_state[index][0]+=line.count('generator')
        intial_state[index][1]+=line.count('microchip')
        total_item+=sum(intial_state[index])

    return next_move_state(intial_state, steps, total_item)
    
def q11_2016_part2():
    input=get_input('11', '2016').splitlines()
    index, steps, total_item=0, 0, 0
    ## state[0]: current floor; state[n]: nth floor's Generator and Chips
    intial_state = [1, [2, 2], [0, 0], [0, 0], [0, 0]]
    for line in input:
        index+=1
        intial_state[index][0]+=line.count('generator')
        intial_state[index][1]+=line.count('microchip')
        total_item+=sum(intial_state[index])

    return next_move_state(intial_state, steps, total_item)
    
def next_move_state(state, steps, total_item):
    steps+=1
    if state[0]==4: # in 4th floor
        if sum(state[4])==total_item: 
            steps+=3
            return steps
        elif state[4][1]: 
            pre_state=[3, state[1], state[2], [state[3][0], state[3][1]+1], [state[4][0], state[4][1]-1], ]
            if isValidMove(pre_state): return next_move_state(pre_state, steps, total_item)
        else:
            pre_state=[3, state[1], state[2], [state[3][0]+1, state[3][1]], [state[4][0]-1, state[4][1]], ] 
            return next_move_state(pre_state, steps, total_item)
    
    elif state[0]==3: # in 3rd floor
        if state[3][0]==0:  # only chips
            if state[3][1]>1:
                pre_state=[4, state[1], state[2], [0, state[3][1]-2], [state[4][0], state[4][1]+2], ]
                return next_move_state(pre_state, steps, total_item)
            else:
                pre_state=[2, state[1], [state[2][0], state[2][1]+1], [0,  0], state[4], ]
                return next_move_state(pre_state, steps, total_item) 
        elif state[3][1]==0: #only generator
            if state[3][0]>1:
                pre_state=[4, state[1], state[2], [state[3][0]-2, 0], [state[4][0]+2, state[4][1]], ]
                return next_move_state(pre_state, steps, total_item)
            else:
                pre_state=[2, state[1], [state[2][0]+1, state[2][1]], [0,  0], state[4], ]
                return next_move_state(pre_state, steps, total_item)  
        else: #mix of generator and chips
                pre_state=[4, state[1], state[2], [state[3][0]-1, state[3][1]-1], [state[4][0]+1, state[4][1]+1], ]
                return next_move_state(pre_state, steps, total_item)      
    elif state[0]==2: # in 2nd floor
        if state[2][0]==0:  # only chips
            if state[2][1]>1:
                pre_state=[3, state[1], [0, state[2][1]-2], [state[3][0], state[3][1]+2], state[4], ]
                if not isValidMove(pre_state):  
                    pre_state[2][1], pre_state[3][1]=pre_state[2][1]+1, pre_state[3][1]-1                    
                return next_move_state(pre_state, steps, total_item)                   
            else:
                pre_state=[1, [state[1][0], state[1][1]+1], [0,  0], state[3], state[4], ]
                return next_move_state(pre_state, steps, total_item) 
        elif state[2][1]==0: #only generator
            if state[2][0]>1:
                pre_state=[3, state[1], [state[2][0]-2, 0], [state[3][0]+2, state[3][1]], state[4], ]
                if not isValidMove(pre_state):  
                    pre_state[2][0], pre_state[3][0]=pre_state[2][0]+1, pre_state[3][0]-1                    
                return next_move_state(pre_state, steps, total_item)                   
            else:
                pre_state=[1, [state[1][0]+1, state[1][1]], [0,  0], state[3], state[4], ]
                return next_move_state(pre_state, steps, total_item)  
        else: #mix of generator and chips
            pre_state=[3, state[1], [state[2][0]-1, state[2][1]-1], [state[3][0]+1, state[3][1]+1],  state[4],]
            if isValidMove(pre_state):
                return next_move_state(pre_state, steps, total_item) 
            if state[2][0]>1:
                pre_state=[3, state[1], [state[2][0]-2, state[2][1]], [state[3][0]+2, state[3][1]],  state[4],]
                if isValidMove(pre_state): return next_move_state(pre_state, steps, total_item) 
            if state[2][1]>1:
                pre_state=[3, state[1], [state[2][0], state[2][1]-2], [state[3][0], state[3][1]+2],  state[4],]
                if isValidMove(pre_state): return next_move_state(pre_state, steps, total_item) 
            pre_state=[3, state[1], [state[2][0]-1, state[2][1]], [state[3][0]+1, state[3][1]],  state[4],]
            if isValidMove(pre_state): return next_move_state(pre_state, steps, total_item) 
            pre_state=[3, state[1], [state[2][0], state[2][1]-1], [state[3][0], state[3][1]+1],  state[4],]
            return next_move_state(pre_state, steps, total_item) 
    elif state[0]==1: # in 1st floor
        if state[1][0]==0:  # only chips
            pre_state=[2, [0, state[1][1]-2], [state[2][0], state[2][1]+2], state[3], state[4], ]
            if not isValidMove(pre_state):  
                pre_state[1][1], pre_state[2][1]=pre_state[1][1]+1, pre_state[2][1]-1                    
            return next_move_state(pre_state, steps, total_item)                   
        elif state[1][1]==0: #only generator
            pre_state=[2, [state[1][0]-2, 0], [state[2][0]+2, state[2][1]], state[3], state[4], ]
            if not isValidMove(pre_state):  
                pre_state[1][0], pre_state[2][0]=pre_state[1][0]+1, pre_state[2][0]-1                    
            return next_move_state(pre_state, steps, total_item)                    
        else: #mix of generator and chips
            pre_state=[2, [state[1][0]-1, state[1][1]-1], [state[2][0]+1, state[2][1]+1], state[3], state[4],]
            if isValidMove(pre_state):
                return next_move_state(pre_state, steps, total_item) 
            if state[1][0]>1:
                pre_state=[2, [state[1][0]-2, state[1][1]], [state[2][0]+2, state[2][1]], state[3], state[4],]
                if isValidMove(pre_state): return next_move_state(pre_state, steps, total_item) 
            if state[1][1]>1:
                pre_state=[2, [state[1][0], state[1][1]-2], [state[2][0], state[2][1]+2], state[3], state[4],]
                if isValidMove(pre_state): return next_move_state(pre_state, steps, total_item) 
            pre_state=[2, [state[1][0]-1, state[1][1]], [state[2][0]+1, state[2][1]], state[3], state[4],]
            if isValidMove(pre_state): return next_move_state(pre_state, steps, total_item) 
            pre_state=[2, [state[1][0], state[1][1]-1], [state[2][0], state[2][1]]+1, state[3], state[4],]
            return next_move_state(pre_state, steps, total_item) 
def isValidMove(state): # check if the move is valid
    #if no generator on current floor or  generator>=chips, its valid
    for i in range(1, 4):
        if state[i][0]>0 and state[i][0]< state[i][1]:
            return False
    return True

####===>  Day 12 Solution <===####
def q12_2016_part1():
    input=get_input('12', '2016').splitlines()
    instr=[]
    for line in input: ## parse each instruction into function string
        line = line.split()
        line.insert(1, '(')
        line.append( ')')
        line.insert(3, ',')
        line=' '.join(line)
        instr.append(line)
    pointer, a, b, c, d=0, [0], [0], [0], [0]
    while -1<pointer<len(instr):
        pointer+=eval(instr[pointer])   
    return(a[0])    

def q12_2016_part2():
    reg = {'a': 0,'b': 0,'c': 1,'d': 0}
    input=get_input('12', '2016').splitlines()
    instr = []
    for line in input:
        instr.append(line.split(' '))        
    pointer = 0
    while True:
        if pointer >= len(instr):
            break
        ins = instr[pointer]
        if ins[0] == 'cpy':
            reg[ins[2]] = get_value(ins[1], reg)
        elif ins[0] == 'inc':
            reg[ins[1]] += 1
        elif ins[0] == 'dec':
            reg[ins[1]] -= 1
        elif ins[0] == 'jnz':
            if get_value(ins[1], reg) != 0:
                pointer += get_value(ins[2], reg)
                pointer -= 1    
        pointer += 1   
    return reg['a']

def get_value(s, reg):
    try: return int(s)
    except ValueError:
        return reg[s]

##define all functions of assembunny code
def cpy(x, y):   
    y[0]=x if isinstance(x, int) else x[0]
    return 1
    
def inc(x):
    x[0]+=1
    return 1
    
def dec(x):
    x[0]-=1
    return 1
   
def jnz(x,y ):
    if isinstance(x, int):
        return y if x!=0 else 1
    return y if x[0]!=0 else 1

####===>  Day 13 Solution <===####
def q13_2016_part1():
    #target 31,39
    input=int(get_input('13', '2016'))
    loc=[[1 for x in range(53)] for y in range(53)]
    ##last row and column are all 1-wall, then no need for 2D list boundary check
    for y in range(52):
        for x in range(52):
            sum=x*x + 3*x + 2*x*y + y + y*y+ input
            # 0-open space  1-wall
            loc[y][x]="{0:b}".format(sum).count('1')%2
    visited, total_step, last_locs={(1,1)}, 0, {(1,1)}
    
    def find_next_move(last_locs, total_step):
        if (31, 39) in visited:
            return total_step
        new_locs=set()
        for last_loc in last_locs:
            (x, y)=last_loc
            ##left neighbour
            if loc[y][x-1]==0 and (x-1, y) not in visited:
                new_locs.add((x-1, y))
            ##right neighbour
            if loc[y][x+1]==0 and (x+1, y) not in visited:
                new_locs.add((x+1, y))
            ##up neighbour
            if loc[y-1][x]==0 and (x, y-1) not in visited:
                new_locs.add((x, y-1))
            ##down neighbour
            if loc[y+1][x]==0 and (x, y+1) not in visited:
                new_locs.add((x, y+1))
        visited.update(new_locs)
        total_step+=1 
        return find_next_move(new_locs, total_step)  

    return find_next_move(last_locs, total_step) 
        
def q13_2016_part2():
    input=int(get_input('13', '2016'))
    loc=[[1 for x in range(53)] for y in range(53)]
    ##last row and column are all 1-wall, then no need for 2D list boundary check
    for y in range(52):
        for x in range(52):
            sum=x*x + 3*x + 2*x*y + y + y*y+ input
            # 0-open space  1-wall
            loc[y][x]="{0:b}".format(sum).count('1')%2
    visited, total_step, last_locs={(1,1)}, 0, {(1,1)}
    
    def find_next_move(last_locs, total_step):
        if total_step==50:
            return
        new_locs=set()
        for last_loc in last_locs:
            (x, y)=last_loc
            ##left neighbour
            if loc[y][x-1]==0 and (x-1, y) not in visited:
                new_locs.add((x-1, y))
            ##right neighbour
            if loc[y][x+1]==0 and (x+1, y) not in visited:
                new_locs.add((x+1, y))
            ##up neighbour
            if loc[y-1][x]==0 and (x, y-1) not in visited:
                new_locs.add((x, y-1))
            ##down neighbour
            if loc[y+1][x]==0 and (x, y+1) not in visited:
                new_locs.add((x, y+1))
        visited.update(new_locs)
        total_step+=1 
        find_next_move(new_locs, total_step)  

    find_next_move(last_locs, total_step)
    return len(visited) 


####===>  Day 14 Solution <===####
def q14_2016_part1():
    ##find 1000 hash first, then start iteration to match the requirement with next 1000 hash
    ##add new hash and remove expired hash
    input=get_input('14', '2016').splitlines()[0]
    keys, candidate, matchs=[], [], [] 
    
    def process_hash(): 
        hash = hashlib.md5((input+str(index)).encode()).hexdigest()            
        for a, b, c in zip(hash, hash[1:], hash[2:]):
            if a==b==c: 
                candidate.append([index, a])
                if any(a==b==c==d==e for a, b, c, d, e in zip(hash, hash[1:], hash[2:], hash[3:], hash[4:])):
                    matchs.append([index, hash])
                return            
    for index in range(1000):
        process_hash()
    while True:
        current=candidate[0]
        for index in range(index+1, current[0]+1001):
            process_hash()
        for match in matchs.copy():
            if match[0]<=current[0]:
                matchs.remove(match)
            elif current[1]*5 in match[1]:
                keys.append(current[0])
                if len(keys)==64: return keys[-1]
                break
        candidate=candidate[1:]
    
def q14_2016_part2():
    ##find 1000 hash first, then start iteration to match the requirement with next 1000 hash
    ##add new hash and remove expired hash
    input=get_input('14', '2016').splitlines()[0]
    keys, candidate, matchs=[], [], [] 
    
    def process_hash():
        hash=input+str(index)
        for i in range(2017):     
            hash = hashlib.md5(hash.encode()).hexdigest()            
        for a, b, c in zip(hash, hash[1:], hash[2:]):
            if a==b==c: 
                candidate.append([index, a])
                if any(a==b==c==d==e for a, b, c, d, e in zip(hash, hash[1:], hash[2:], hash[3:], hash[4:])):
                    matchs.append([index, hash])
                return            
    for index in range(1000):
        process_hash()
    while True:
        current=candidate[0]
        for index in range(index+1, current[0]+1001):
            process_hash()
        for match in matchs.copy():
            if match[0]<=current[0]:
                matchs.remove(match)
            elif current[1]*5 in match[1]:
                keys.append(current[0])
                if len(keys)==64: return keys[-1]
                break
        candidate=candidate[1:]

####===>  Day 15 Solution <===####
def q15_2016_part1():      
    input=get_input('15', '2016').splitlines()
    discs, max_disc=[], [0, 0]
    for line in input:
        line=line.split()
        discs.append([int(line[3]), int(line[-1][:-1])])
        if int(line[3])>max_disc[0]: max_disc=discs[-1]
    i_max=discs.index(max_disc)
    discs=discs[:i_max]+[[disc[0], disc[1]+1] for disc in discs[i_max+1:]]
    ## find disc with max positions and use it to generate candidate time which
    ## could cut down complexity to 1/max_posotion
    for time in range(max_disc[0]-max_disc[1]-i_max-1, 10000000, max_disc[0]):
        i_disc=0
        for disc in discs:
            if (time+1+i_disc+disc[1])%disc[0]==0: i_disc+=1
            else: break
            
        if i_disc==len(discs) :  return time 
        
def q15_2016_part2():      
    input=get_input('15', '2016').splitlines()
    discs, max_disc=[], [0, 0]
    for line in input:
        line=line.split()
        discs.append([int(line[3]), int(line[-1][:-1])])
        if int(line[3])>max_disc[0]: max_disc=discs[-1]
    i_max=discs.index(max_disc)
    discs=discs[:i_max]+[[disc[0], disc[1]+1] for disc in discs[i_max+1:]]
    discs.append([11,1])
    ## find disc with max positions and use it to generate candidate time which
    ## could cut down complexity to 1/max_posotion
    for time in range(max_disc[0]-max_disc[1]-i_max-1, 10000000, max_disc[0]):
        i_disc=0
        for disc in discs:
            if (time+1+i_disc+disc[1])%disc[0]==0: i_disc+=1
            else: break
            
        if i_disc==len(discs) :  return time 

####===>  Day 16 Solution <===####
def q16_2016_part1():
    return find_checksum(272)

def q16_2016_part2():
    return find_checksum(35651584)

def find_checksum(disk_len):    
    input=get_input('16', '2016').splitlines()[0] 
    ## flip of 10010 is 11111-10010= 01101 which is quick faster than string conversion
    while len(input)<disk_len:
        flip="{0:b}".format(int('1'*len(input), 2)-int(input[::-1], 2))
        flip='0'*(len(input)-len(flip))+flip
        input=input+'0'+flip
    input=input[:disk_len]
    
    while len(input)%2==0:
        checksum=''
        for i in range(0, len(input), 2):
            checksum+='1' if input[i]==input[i+1] else '0'
        input=checksum          
    return checksum

####===>  Day 17 Solution <===####
def q17_2016_part1():
    input=get_input('17', '2016').splitlines()[0]
    init_rm, init_path, min_path=1, '', ['D'*100]
    valid_rm=[1,2,3,4,7,8,9,10,13,14,15,16,19,20,21]
    
    def next_room(path, rm_index, min_path):
        if rm_index==22: # found one path
            if len(path)<len(min_path[0]):
               min_path[0]= path
            return         
        if rm_index in valid_rm and len(path)<len(min_path[0]): #invalid room or path more than min_path
            ins=hashlib.md5((input+path).encode()).hexdigest()[:4]
            if ins[0] in 'bcdef':
                next_room(path+'U', rm_index-6, min_path)
            if ins[1] in 'bcdef':
                next_room(path+'D', rm_index+6, min_path)
            if ins[2] in 'bcdef':
                next_room(path+'L', rm_index-1, min_path)
            if ins[3] in 'bcdef':
                next_room(path+'R', rm_index+1, min_path)
    
    next_room(init_path, init_rm, min_path)    
    return min_path[0]

def q17_2016_part2():
    input=get_input('17', '2016').splitlines()[0]
    init_rm, init_path, max_path=1, '', ['D']
    valid_rm=[1,2,3,4,7,8,9,10,13,14,15,16,19,20,21]
    
    def next_room(path, rm_index, max_path):
        if rm_index==22: # found one path
            if len(path)>len(max_path[0]):
               max_path[0]= path
            return         
        if rm_index in valid_rm : #invalid room or path more than max_path
            ins=hashlib.md5((input+path).encode()).hexdigest()[:4]
            if ins[0] in 'bcdef':
                next_room(path+'U', rm_index-6, max_path)
            if ins[1] in 'bcdef':
                next_room(path+'D', rm_index+6, max_path)
            if ins[2] in 'bcdef':
                next_room(path+'L', rm_index-1, max_path)
            if ins[3] in 'bcdef':
                next_room(path+'R', rm_index+1, max_path)
    
    next_room(init_path, init_rm, max_path)    
    return len(max_path[0])

####===>  Day 18 Solution <===####
def q18_2016_part1():
    input=get_input('18', '2016').splitlines()[0]
    col, count=len(input), input.count('.')
    flr=['.'+input+'.']
    trap=['..^', '.^^', '^..', '^^.']
    for i in range(1, 40):
        row='.'
        for j in range(col):
            row+='^' if flr[i-1][j:j+3] in trap else '.'
        count+=row.count('.')-1
        row+='.'
        flr.append(row)    
    return count 

def q18_2016_part2():
    input=get_input('18', '2016').splitlines()[0]
    col, count=len(input), input.count('.')
    flr=['.'+input+'.']
    trap=['..^', '.^^', '^..', '^^.']
    for i in range(1, 400000):
        row='.'
        for j in range(col):
            row+='^' if flr[i-1][j:j+3] in trap else '.'
        count+=row.count('.')-1
        row+='.'
        flr.append(row)   
    return count      

####===>  Day 19 Solution <===####
def q19_2016_part1():
    input=int(get_input('19', '2016').splitlines()[0])
    elfs=[i for i in range(1, input+1)]
    while len(elfs)>1:
        is_odd=len(elfs)%2
        elfs = elfs[::2]
        if is_odd: elfs=elfs[1:]
    return elfs[0]

def q19_2016_part2():
    input=int(get_input('19', '2016').splitlines()[0])
    elfs=deque([i for i in range(input//2+2, input+1)]+[j for j in range(1, input//2+2)])
    ## using deque to pop and rotate is much faster than list removal    
    for i in range(len(elfs),1, -1):
        if i%2: #odd elfs  [4,5,1,2,3]
            elfs.pop()
            elfs.rotate(-2)
        else:  # even elfs [1,2,4,5]
            elfs.pop()
            elfs.rotate(-1)
    return elfs[0]

####===>  Day 20 Solution <===####
def q20_2016_part1():
    input=get_input('20', '2016').splitlines()
    ip_range={}
    for line in input:
        [low, up]=line.split('-')
        ip_range[int(low)]=int(up)
    ip_range=OrderedDict(sorted(ip_range.items()))
    def find_upper(pre_up):
        new_up=pre_up
        for low ,up in ip_range.copy().items():
            if up<=pre_up:
                del ip_range[low]
            elif low<pre_up+2:
                new_up= max(new_up, up)
                del ip_range[low]
        if new_up==pre_up: return new_up
        return find_upper(new_up)                        
    return find_upper(ip_range[0])+1
 
def q20_2016_part2():
    input=get_input('20', '2016').splitlines()
    ip_range={}
    for line in input:
        [low, up]=line.split('-')
        ip_range[int(low)]=int(up)
    ip_range=OrderedDict(sorted(ip_range.items()))
    
    def find_upper(pre_up):
        new_up=pre_up
        for low ,up in ip_range.copy().items():
            if up<=pre_up:
                del ip_range[low]
            elif low<pre_up+2:
                new_up= max(new_up, up)
                del ip_range[low]
        if new_up==pre_up: return new_up
        return find_upper(new_up)
    
    count, low=0, list(ip_range.items())[0][0]
    while len(ip_range):                     
        up=find_upper(low)
        if len(ip_range):
            low= list(ip_range.items())[0][0]
        else: low=4294967295+1
        count+=low- up-1 
         
    return count 

####===>  Day 21 Solution <===####
def q21_2016_part1():
    input=get_input('21', '2016').splitlines()
    s='abcdefgh'
    for line in input:
        ins=line.split()
        if ins[0]=='swap': 
            if ins[1]=='position': #case swap position
                s=swap_position(s, int(ins[2]), int(ins[-1]))
            else: # case swap_letter
                s=swap_letter(s, ins[2], ins[-1])
        elif ins[0]=='rotate':
            if ins[1]=='based': #case rotate based on position
                s=rotate_pos(s, ins[6])
            else: # case rotate left/right
                s=rotate(s, ins[1], int(ins[2]))
        elif ins[0]=='reverse':s=reverse_pos(s, int(ins[2]), int(ins[4]))
        else: s=move_pos(s, int(ins[2]), int(ins[5]))
    return s

def q21_2016_part2():
    input=get_input('21', '2016').splitlines()
    s='fbgdceah'
    move_map={}
    for i in range(len(s)): # build mapping for case rotate based on position
        move_map[(2*i+ (1 if i<4 else 2))%len(s)]=(i+ (1 if i<4 else 2))%len(s)        
    for line in reversed(input):
        ins=line.split()
        if ins[0]=='swap': # remains same for part 2
            if ins[1]=='position': #case swap position
                s=swap_position(s, int(ins[2]), int(ins[-1]))
            else: # case swap_letter
                s=swap_letter(s, ins[2], ins[-1])
        elif ins[0]=='rotate':
            if ins[1]=='based': #case rotate based on position
                s=rotate_pos2(s, ins[6],move_map)
            else: # case rotate left/right, just toggle left/right             
                s=rotate(s, 'leftright'.replace(ins[1], ''), int(ins[2]))
        elif ins[0]=='reverse':s=reverse_pos(s, int(ins[2]), int(ins[4]))
        else: s=move_pos(s, int(ins[5]), int(ins[2])) # swap x and y
    return s

def swap_position(s, x, y):
    l=list(s)
    l[x], l[y]= l[y], l[x]
    return ''.join(l)
def swap_letter(s, x, y):
    s=s.replace(x,'*')
    s=s.replace(y, x)
    return s.replace('*', y)
def rotate(s, d, x):
    if d=='left': return s[x:]+s[:x]
    return s[-x:]+s[:-x]
def rotate_pos(s, x):
    i= s.find(x)
    move= (i+ (1 if i<4 else 2))%len(s)
    return s[-move:]+s[:-move]
def rotate_pos2(s, x, move_map): #for part 2 using build mapping
    move= move_map[s.find(x)]
    return s[move:]+s[:move]
def reverse_pos(s, x, y):
    if x: return s[:x]+s[y:x-1:-1] +s[y+1:]
    return s[y::-1] +s[y+1:]
def move_pos(s, x, y):
    if x<y: return s[:x]+s[x+1:y+1]+s[x]+('' if y==len(s)-1 else s[y+1:])
    else:   return s[:y]+s[x]+s[y:x]+('' if x==len(s)-1 else s[x+1:])

####===>  Day 22 Solution <===####
def q22_2016_part1():
    input=get_input('22', '2016').splitlines()
    used, avail=[], []
    count=0
    for line in input[2:]:
        data= line.split()
        used.append(int(data[2][:-1])) 
        avail.append(int(data[3][:-1]))
        if 0<used[-1]<=avail[-1]: count-=1        
    used, avail=sorted(used), sorted(avail)
    j=0
    for i in range(1, len(used)): # 1st is not used
        while used[i]>avail[j]:
            j+=1
            if j==len(avail): return count
        count+=len(avail)-j
    return count 

def q22_2016_part2():
    input=get_input('22', '2016').splitlines()
    nodes=[['.' for x in range(33)] for y in range(30)]
    count, x_, y_, x_G, y_G= 0, 0, 0, 32, 0
    for line in input[2:]:
        data= line.split()
        size, used, avail=int(data[1][:-1]), int(data[2][:-1]), int(data[3][:-1])
        if used>100: nodes[count%30][count//30] ='#'
        elif used==0: 
            x_, y_=count//30, count%30
            nodes[y_][x_] ='_'
        count+=1
    nodes[y_G][x_G]='G'
#     for row in nodes: #after print, find x=3, y=27 is the connection for shortest path
#         print(row)
    step=0
    while True:
        if y_G==x_G==0: return step
        if x_>x_G: step+=5
        else: step+=x_G-3+x_-3 + y_-y_G
        x_, y_, x_G=x_G, y_G, x_G-1
        
####===>  Day 23 Solution <===####
def q23_2016_part1():
    reg = {'a': 7,'b': 0,'c': 0,'d': 0}
    input=get_input('23', '2016').splitlines()
    instr = []
    for line in input:
        instr.append(line.split(' '))        
    pointer, total = 0, len(instr)
    while True:
        if pointer >= total or pointer<0:
            return reg['a']
        ins = instr[pointer]
        if ins[0] == 'cpy':
            reg[ins[2]] = get_value(ins[1], reg)
        elif ins[0] == 'inc':
            reg[ins[1]] += 1
        elif ins[0] == 'dec':
            reg[ins[1]] -= 1
        elif ins[0] == 'jnz':
            if get_value(ins[1], reg) != 0:
                pointer += get_value(ins[2], reg)-1
        elif ins[0] == 'tgl':
            target_i= pointer+reg[ins[1]]
            if -1<target_i<total:
                ins = instr[target_i]
                if len(ins)==2:
                    ins[0]='dec' if ins[0]=='inc' else 'inc'
                else:
                    ins[0]='cpy' if ins[0]=='jnz' else 'jnz'
        pointer += 1

def q23_2016_part2():
    '''
    need find out repeated pattern by printing out the pointer movement
    '''
    reg = {'a': 12,'b': 0,'c': 0,'d': 0}
    input=get_input('23', '2016').splitlines()
    instr = []
    for line in input:
        instr.append(line.split(' '))        
    pointer, total = 0, len(instr)
    while True:
        if pointer >= total or pointer<0:
            return reg['a']      
        if pointer==4: #line 4-9 is actually doing a=a+b*d
            reg['a']+=reg['b']*reg['d']
            reg['c'], reg['d']=0, 0
            pointer=10
            continue
        if pointer==20: #line 20-25 is actually doing a=a+77*c
            reg['a']+=77* reg['c']
            reg['d'], reg['c']=0, 0
            pointer=26
            continue
        ins = instr[pointer]
        if ins[0] == 'cpy':
            reg[ins[2]] = get_value(ins[1], reg)
        elif ins[0] == 'inc':
            reg[ins[1]] += 1
        elif ins[0] == 'dec':
            reg[ins[1]] -= 1
        elif ins[0] == 'jnz':
            if get_value(ins[1], reg) != 0:
                pointer += get_value(ins[2], reg)-1
        elif ins[0] == 'tgl':
            target_i= pointer+reg[ins[1]]
            if -1<target_i<total:
                ins = instr[target_i]
                if len(ins)==2:
                    ins[0]='dec' if ins[0]=='inc' else 'inc'
                else:
                    ins[0]='cpy' if ins[0]=='jnz' else 'jnz'
        pointer += 1

####===>  Day 24 Solution <===####
def q24_2016_part1():
    return q24_2016(part2=[False])

def q24_2016_part2():
    return q24_2016(part2=[True])

def q24_2016(part2):
    input =get_input('24', '2016').splitlines()
    maze, target, dist=[], set(), {}
    for line in input:
        maze.append(list(line))
        for match in re.finditer(r'[0-7]+', line):
            if match.group()=='0': orgin=(match.start(), input.index(line))            
            target.add((match.start(), input.index(line)))
    ## find shortest steps starting from a passage to other passage        
    def find_next_move(last_locs, total_step):
        found=target & last_locs
        if found:
            for psg in found: all_found[psg]= total_step
            if len(all_found)==len(target): return all_found
        new_locs=set()
        for last_loc in last_locs:
            (x, y)=last_loc
            if maze[y][x-1]!='#' and (x-1, y) not in visited:
                new_locs.add((x-1, y))
            if maze[y][x+1]!='#' and (x+1, y) not in visited:
                new_locs.add((x+1, y))
            if maze[y-1][x]!='#' and (x, y-1) not in visited:
                new_locs.add((x, y-1))
            if maze[y+1][x]!='#' and (x, y+1) not in visited:
                new_locs.add((x, y+1))     
        visited.update(new_locs)
        total_step+=1 
        return find_next_move(new_locs, total_step)
     
    for pos in target: ## build distance dict for all passage
        total_step, visited, last_locs, all_found=0, {pos},  {pos}, {}
        pos_dist=find_next_move(last_locs, total_step)
        del pos_dist[pos]
        dist[pos]=pos_dist
    ## find min steps to visit all target    
    steps, min_steps, visited=0, [10000], [orgin]
    def find_min_steps(last_visit, visited, steps):
        if steps>min_steps[0]: return
        if len(visited)==len(target): 
            if part2[0]: steps+=dist[last_visit][orgin]
            min_steps[0]=min(min_steps[0], steps)
            return
        for pos, distance in dist[last_visit].items():
            if pos not in visited: 
                new_visited=visited.copy()
                new_visited.append(pos)
                step_new=steps+distance
                find_min_steps(pos, new_visited, step_new)
    
    find_min_steps(orgin, visited, steps)
    return min_steps[0]

####===>  Day 25 Solution <===####
def q25_2016_part1():
    input=get_input('25', '2016').splitlines()
    instr = []
    for line in input:
        instr.append(line.split(' '))        
    init_a= 0
    counter=[0 for i in range(len(instr))] # use this to find pattern of assembunny code
    
    while True: ## test a from 0 until success
        pointer, output=0, []
        init_a+=1
        reg = {'a': init_a,'b': 0,'c': 0,'d': 0}
        ##loop stops once output is not toggling, then test a+1
        while True: 
            if pointer==1: #line 1-7 is actually doing d=d+633*4
                reg['d']+=4*633
                reg['b'], reg['c']=0, 0
                pointer=8
                continue        
            if pointer==12: #line 12-19 performs b//2 and b%2
                reg['a']+=reg['b']//2
                reg['c']=2-reg['b']%2
                reg['b']= 0
                pointer=20
                continue
            ins = instr[pointer]
            #counter[pointer]+=1 # use this counter to find the pattern
            if ins[0] == 'cpy':
                reg[ins[2]] = get_value(ins[1], reg)
            elif ins[0] == 'inc':
                reg[ins[1]] += 1
            elif ins[0] == 'dec':
                reg[ins[1]] -= 1
            elif ins[0] == 'jnz':
                if get_value(ins[1], reg) != 0:
                    pointer += get_value(ins[2], reg)-1
            elif ins[0] == 'out':
                #failed if new output repeats last output
                if output and output[-1]==reg[ins[1]]: break
                if len(output)>100: #assume successful if 100 output follow clock signal pattern
                    return init_a
                output.append(reg[ins[1]])
            pointer += 1          

def q25_2016_part2():
    return 'All done for 25 days of 2016'
     
###########  Execution  ############# 
# start_time=time.time()
# result=q25_2016_part1()
# end_time=time.time()
# print('result:',result ,'|| execution time: %s s'%"{:.2f}".format(end_time-start_time))

