# -*- coding: utf-8 -*-
import re
import time
from itertools import permutations, combinations
from math import factorial, ceil
from collections import Counter
import hashlib 
from pandas.core.strings import str_index
import copy
from turtledemo.sorting_animate import instructions1
from werkzeug.wsgi import responder

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
    for i in range(0, len(screen[0]), 5):
        
        for row in screen:
            print(row[i:i+5])
        print('================')

    
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
              
###########  Execution  ############# 
start_time=time.time()
result=q10_2016_part2()
end_time=time.time()
print('result:',result ,'|| execution time: %s s'%"{:.2f}".format(end_time-start_time))

