
from util import read_file
from functools import reduce
import hashlib
import string
import re
import pandas as pd
import itertools


############################## Day 1 ##############################
def day1part1():
    mystring = read_file("1", "string")
    floor = 0
    for i in mystring: 
        if i == '(':
            floor += 1
        elif i ==')':
            floor -= 1
    return floor

def day1part2():
    floor = 0
    mylist = read_file("1", "list")
    list_floor = tuple(mylist[0])
    for index, value in enumerate(list_floor): 
        if value == '(':
            floor += 1
        elif value ==')':
            floor -= 1
            if floor ==-1: 
                return index+1

############################## Day 2 ##############################
def day2part1():
    mylist = read_file("2", "list")
    results=[]
    for box in mylist:
        boxspec=box.rstrip().split("x")
        boxspecint=list(map(int, boxspec))
        allfaces=(boxspecint[0]*boxspecint[1]+boxspecint[0]*boxspecint[2]+boxspecint[1]*boxspecint[2])*2
        smallestface=min([boxspecint[0]*boxspecint[1], boxspecint[0]*boxspecint[2], boxspecint[1]*boxspecint[2]])
        # get individual result
        result=allfaces+smallestface
        results.append(result)
    #get final results
    calnum=reduce((lambda x,y:x+y), results)
    return calnum

def day2part2():
    mylist = read_file("2", "line")
    results=[]
    for box in mylist:
        boxspec=box.rstrip().split("x")
        boxspecint=list(map(int, boxspec))
        boxspecint.sort()
        ribbonwrap=(boxspecint[0]+boxspecint[1])*2
        ribbonbowl=reduce((lambda x, y: x *y), boxspecint)
        ribbonall=ribbonwrap+ribbonbowl
        results.append(ribbonall)
    calnum=reduce((lambda x,y:x+y), results)
    return calnum

############################## Day 3 ##############################
def day3part1():
    allarrows = read_file("3", "string")
    x = 0
    y = 0
    origin = [(x,y)]
    for i in allarrows:
        if i == ">":
            x += 1
        elif i =="<":
            x -= 1
        elif i == "^":
            y += 1
        elif i == "v":
            y -= 1
        origin.append((x,y))
    unique_value = list(set(origin))
    return len(unique_value)

def day3part2():
    allarrows = read_file("3", "string")
    # get each individual arrows
    santaarrows = allarrows[0:len(allarrows):2]
    robotarrows = allarrows[1:len(allarrows):2]
    # return each one list
    santalist = oneperson(santaarrows)
    robolist = oneperson(robotarrows)
    # add up to one list
    finallist = santalist + robolist
    finaluniquelist = list(set(finallist))
    return len(finaluniquelist)

def oneperson(arrows):
    x = 0
    y = 0
    origin = [(x,y)]
    for i in arrows:
        if i == ">":
            x += 1
        elif i =="<":
            x -= 1
        elif i == "^":
            y += 1
        elif i == "v":
            y -= 1
        origin.append((x,y))
    return origin

############################## Day 4 ##############################
def day4part1():
    initValue = read_file("4", "string")
    calculate(initValue, "00000")

def calculate(initValue, target):
    restValue = 0
    goal = False
    while goal != True:
        # check if hash value match the 00000
        result = initValue + str(restValue)
        h = hashlib.md5(result.encode())
        hexvalue = h.hexdigest()
        goal = True if hexvalue[0:len(target)] == target else False
        restValue += 1
    if goal:
        return restValue

def day4part2():
    initValue = read_file("4", "string")
    calculate(initValue, "000000")

############################## Day 5 ##############################
def day5part1():
    # get ready the starting double letter and sequence
    atoz = list(string.ascii_lowercase)
    listdouble = list(map(lambda el: el+el, atoz))
    listsequence =["ab", "cd", "pq", "xy"]
    mylist = read_file("5", "list")
    def isNice(eachstr):
        vowelsCount = list(filter(lambda x: x in ["a","e","i","o","u"], list(eachstr)))
        # check if have double letter
        sameLetters = True if True in list(map(lambda x: x in eachstr, listdouble)) else False
        # check if have sequence letter
        sequenceletters = True if True in list(map(lambda x: x in eachstr, listsequence)) else False
        # return 1 if it meets nice criteria
        if len(vowelsCount)>2 and sameLetters and not sequenceletters :
            return 1
        else:
            return 0
    result = reduce(lambda a,b: a+b, list(map(isNice, mylist)))
    return result

def day5part2():
    mylist = read_file("5", "list")
    def isNice(eachstr):
        # use regex to construct the pattern
        repeatpattern = re.compile(r"([a-z][a-z]).*\1")
        repeat = repeatpattern.search(eachstr)
        # use regex to construct the pattern
        sandwichpattern = re.compile(r"([a-z]).\1")
        sandwich = sandwichpattern.search(eachstr)
        if repeat and sandwich  :
            return 1
        else:
            return 0
    result = reduce(lambda a,b: a+b, list(map(isNice, mylist)))
    return result

############################## Day 6 ##############################
def day6part1():
    lights = pd.DataFrame(0, range(0,1000), range(0,1000))
    def turnon(x1,y1,x2,y2): 
        lights.loc[x1:x2,y1:y2] = 1
    def turnoff(x1,y1,x2,y2):
        lights.loc[x1:x2,y1:y2] = 0
    def toggle(x1,y1,x2,y2):
        lights.loc[x1:x2,y1:y2] = (lights.loc[x1:x2,y1:y2] + 1) % 2
    
    my_list = read_file('6', "list")
    for line in my_list:
        numstr = re.findall(r'\d+',line)
        num = list(map(lambda x: int(x),numstr)) # need to change to int otherwise has some parsing issue
        if 'on' in line:
            turnon(*num)
        elif 'off' in line:
            turnoff(*num)
        elif "toggle" in line:
            toggle(*num)
    return lights.values.sum()

def day6part2():
    lights = pd.DataFrame(0, range(0,1000), range(0,1000))
    def turnon(x1,y1,x2,y2): 
        lights.loc[x1:x2,y1:y2] += 1
    def turnoff(x1,y1,x2,y2):
        # use applymap to map individual cell
        lights.loc[x1:x2,y1:y2] = lights.loc[x1:x2,y1:y2].applymap(lambda x: x-1 if x > 0 else 0)
    def toggle(x1,y1,x2,y2):
        lights.loc[x1:x2,y1:y2] += 2

    my_list = read_file('6', "list")
    for line in mylist:
        numstr = re.findall(r'\d+',line)
        num = list(map(lambda x: int(x),numstr)) # need to change to int otherwise has some parsing issue
        if 'on' in line:
            turnon(*num)
        elif 'off' in line:
            turnoff(*num)
        elif "toggle" in line:
            toggle(*num)
    return lights.values.sum()

############################## Day 7 ##############################
def day7part1():
    mydict = {}
    def andOperator(linelist,fulllist): 
        var1 = linelist[0]
        var2 = linelist[2]
        varlast = linelist[-1]
        if var1 in mydict and var2 in mydict:
            mydict[varlast] = int(mydict[var1]) & int(mydict[var2])
            fulllist.remove(" ".join(linelist))
        elif var1.isdigit() and var2 in mydict:
            mydict[varlast] = int(var1) & int(mydict[var2])
            fulllist.remove(" ".join(linelist))
        elif var2.isdigit() and var1 in mydict:
            mydict[varlast] = int(var2) & int(mydict[var1])
            fulllist.remove(" ".join(linelist))
        elif var1.isdigit() and var2.isdigit():
            mydict[varlast] = int(var1) & int(var2)
            fulllist.remove(" ".join(linelist))
    def orOperator(linelist,fulllist):
        var1 =linelist[0]
        var2 =linelist[2]
        varlast = linelist[-1]
        if var1 in mydict and var2 in mydict:
            mydict[varlast] = int(mydict[var1]) | int(mydict[var2])
            fulllist.remove(" ".join(linelist))

        elif var1.isdigit() and var2 in mydict:
            mydict[varlast] = int(var1) | int(mydict[var2])
            fulllist.remove(" ".join(linelist))

        elif var2.isdigit() and var1 in mydict:
            mydict[varlast] = int(var2) | int(mydict[var1])
            fulllist.remove(" ".join(linelist))
        elif var1.isdigit() and var2.isdigit():
            mydict[varlast] = int(var1) | int(var2)
            fulllist.remove(" ".join(linelist))
    def rshiftOperator(linelist,fulllist):
        var1 =linelist[0]
        var2 =linelist[2]
        varlast = linelist[-1]
        if var1 in mydict and var2.isdigit():
            mydict[varlast] =int(mydict[var1]) >> int(var2)
            fulllist.remove(" ".join(linelist))
    def lshiftOperator(linelist,fulllist):
        var1 =linelist[0]
        var2 =linelist[2]
        varlast = linelist[-1]
        if var1 in mydict and var2.isdigit():
            mydict[varlast] = int(mydict[var1]) << int(var2)
            fulllist.remove(" ".join(linelist))
    def notOperator(linelist,fulllist):
        var1 =linelist[1]
        varlast = linelist[-1]
        if var1 in mydict:
            mydict[varlast] = ~int(mydict[var1])
            fulllist.remove(" ".join(linelist))
    def assign(linelist,fulllist):
        var1 = linelist[0]
        varlast = linelist[-1]
        if var1.isdigit():
            mydict[varlast] = int(var1)
            fulllist.remove(" ".join(linelist))
        elif var1 in mydict:
            mydict[varlast] = int(mydict[var1])
            fulllist.remove(" ".join(linelist))
    def checkLogic(fulllist,count):
        # add a breaker to not go infinite loop, play with the number
        count += 1
        if count > 200: 
            print("stop by count")
            return "stop "
        if fulllist:
            for line in fulllist:
                linelist = line.rstrip().split(" ")
                if "AND" in line:
                    andOperator(linelist,fulllist)
                elif "NOT" in line:
                    notOperator(linelist,fulllist)
                elif "OR" in line:
                    orOperator(linelist,fulllist)
                elif "RSHIFT" in line:
                    rshiftOperator(linelist,fulllist)
                elif "LSHIFT" in line:
                    lshiftOperator(linelist,fulllist)
                else: 
                    assign(linelist,fulllist)
            checkLogic(fulllist,count)
        else:
            print(f"list is empty, end with result {mydict['a']}")

    mylist = read_file('7', "list")
    checkLogic(mylist, 1)
    return mydict['a']

def day7part2():
    mydict = {}
    def assign(linelist,fulllist):
        var1 = linelist[0]
        varlast = linelist[-1]
        if varlast == "b":
            mydict["b"] = 956
            fulllist.remove(" ".join(linelist))
        if var1.isdigit() and varlast != "b":
            mydict[varlast] = int(var1)
            fulllist.remove(" ".join(linelist))
        elif var1 in mydict:
            mydict[varlast] = int(mydict[var1])
            fulllist.remove(" ".join(linelist))
    def andOperator(linelist,fulllist): 
        var1 = linelist[0]
        var2 = linelist[2]
        varlast = linelist[-1]
        if var1 in mydict and var2 in mydict:
            mydict[varlast] = int(mydict[var1]) & int(mydict[var2])
            fulllist.remove(" ".join(linelist))
        elif var1.isdigit() and var2 in mydict:
            mydict[varlast] = int(var1) & int(mydict[var2])
            fulllist.remove(" ".join(linelist))
        elif var2.isdigit() and var1 in mydict:
            mydict[varlast] = int(var2) & int(mydict[var1])
            fulllist.remove(" ".join(linelist))
        elif var1.isdigit() and var2.isdigit():
            mydict[varlast] = int(var1) & int(var2)
            fulllist.remove(" ".join(linelist))
    def orOperator(linelist,fulllist):
        var1 =linelist[0]
        var2 =linelist[2]
        varlast = linelist[-1]
        if var1 in mydict and var2 in mydict:
            mydict[varlast] = int(mydict[var1]) | int(mydict[var2])
            fulllist.remove(" ".join(linelist))

        elif var1.isdigit() and var2 in mydict:
            mydict[varlast] = int(var1) | int(mydict[var2])
            fulllist.remove(" ".join(linelist))

        elif var2.isdigit() and var1 in mydict:
            mydict[varlast] = int(var2) | int(mydict[var1])
            fulllist.remove(" ".join(linelist))
        elif var1.isdigit() and var2.isdigit():
            mydict[varlast] = int(var1) | int(var2)
            fulllist.remove(" ".join(linelist))
    def rshiftOperator(linelist,fulllist):
        var1 =linelist[0]
        var2 =linelist[2]
        varlast = linelist[-1]
        if var1 in mydict and var2.isdigit():
            mydict[varlast] =int(mydict[var1]) >> int(var2)
            fulllist.remove(" ".join(linelist))
    def lshiftOperator(linelist,fulllist):
        var1 =linelist[0]
        var2 =linelist[2]
        varlast = linelist[-1]
        if var1 in mydict and var2.isdigit():
            mydict[varlast] = int(mydict[var1]) << int(var2)
            fulllist.remove(" ".join(linelist))
    def notOperator(linelist,fulllist):
        var1 =linelist[1]
        varlast = linelist[-1]
        if var1 in mydict:
            mydict[varlast] = ~int(mydict[var1])
            fulllist.remove(" ".join(linelist))
    def checkLogic(fulllist,count):
        # add a breaker to not go infinite loop, play with the number
        count += 1
        if count > 200: 
            print("stop by count")
            return "stop "
        if fulllist:
            for line in fulllist:
                linelist = line.rstrip().split(" ")
                if "AND" in line:
                    andOperator(linelist,fulllist)
                elif "NOT" in line:
                    notOperator(linelist,fulllist)
                elif "OR" in line:
                    orOperator(linelist,fulllist)
                elif "RSHIFT" in line:
                    rshiftOperator(linelist,fulllist)
                elif "LSHIFT" in line:
                    lshiftOperator(linelist,fulllist)
                else: 
                    assign(linelist,fulllist)
            checkLogic(fulllist,count)
        else:
            print(f"list is empty, end with result {mydict['a']}")
            return mydict['a']

    mylist = read_file('7', "list")
    checkLogic(mylist, 1)
    return mydict['a']

############################## Day 8 ##############################
def day8part1():
    def checkeachline(line):
        fulllength = len(line)
        # remove hex value
        hexvalue = re.findall(r'\\x[0-9,a-f][0-9,a-f]',line)
        if hexvalue:
            for el in hexvalue:
                line = line.replace(el,'!')
        backslash = re.findall(r'\\.', line)
        if backslash:
            for el in backslash:
                line = line.replace(el,'~')
        strlength = len(line)-2
        return (fulllength, strlength)
    
    mylist = read_file('8', 'list') 
    fulllength = []
    strlength = []
    for line in mylist:
        result = checkeachline(line)
        fulllength.append(result[0])
        strlength.append(result[1])
    return sum(fulllength)-sum(strlength)

def day8part2():
    def checkeachline(line):
        fulllength = len(line)
        # remove hex value
        hexvalue = re.findall(r'\\x[0-9,a-f][0-9,a-f]',line)
        if hexvalue:
            for el in hexvalue:
                line = line.replace(el,'!!!!!')
        backslash = re.findall(r'\\.', line)
        if backslash:
            for el in backslash:
                line = line.replace(el,'~~~~')
        strlength = len(line)+4
        return (fulllength, strlength)
    
    mylist = read_file('8', 'list') 
    fulllength = []
    strlength = []
    for line in mylist:
        result = checkeachline(line)
        fulllength.append(result[0])
        strlength.append(result[1])
    return sum(strlength)-sum(fulllength)

############################## Day 9 ##############################
def day9():
    def getDistanceList():
        distanceList = []
        Stations = []
        mylist = read_file('9','list')
        for line in mylist:
            linelist = line.rstrip().split()[::2]
            Stations.extend(linelist[:2])
            distanceList.append(linelist)
        allStations = list(set(Stations))
        return distanceList, allStations

    def calculateDistance(route, distanceList):
        distanceValue = 0
        for i in range(len(route)-1):
            for distance in distanceList:
                if route[i] in distance and route[i+1] in distance:
                    distanceValue += int(distance[2])
        return distanceValue
    results =[]
    distanceList, allStations = getDistanceList()
    # create all stations permutations to use to iterate
    allPermutations = list(itertools.permutations(allStations))
    # calculate each distance and push to results list
    for route in allPermutations:
        results.append(calculateDistance(route, distanceList))
    return results

def day9part1():
    return min(day9())
    
def day9part2():
    return max(day9())

############################## Day 10 ##############################
def day9_getNextValue(value):
    results = []
    point = 0
    for index, letter in enumerate(value):
        if index < len(value)-1:
            # in case next number is different
            if letter != value[index+1]:
                points = point+1
                results.append(str(points)+letter)
                point = 0
            # in case next number is the same, add 1 point to point, to use later
            else:
                point += 1
                continue
        # use elif to handle last value
        elif value[-2] != value[-1]:
            results.append("1"+value[-1])
        elif value[-2] == value[-1]:
            results.append(str(point+1)+value[-1])
    strResult = "".join(results)
    return strResult

def day10part1():
    values = ["3113322113"]
    times = 40 
    for i in range(times):
        values.append(day9_getNextValue(values[i]))
    return len(values[-1])

def day10part2():
    values = ["3113322113"]
    times = 50 
    for i in range(times):
        values.append(day9_getNextValue(values[i]))
    return len(values[-1])

print(day10part2())

