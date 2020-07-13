import sys
sys.path.append("./lib")

from util import read_file
from functools import reduce
import hashlib
import string
import re
import pandas as pd
import itertools
import json
import math
import collections


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
    return calculate(initValue, "00000")

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
    return calculate(initValue, "000000")

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
    return int(lights.values.sum())

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
    for line in my_list:
        numstr = re.findall(r'\d+',line)
        num = list(map(lambda x: int(x),numstr)) # need to change to int otherwise has some parsing issue
        if 'on' in line:
            turnon(*num)
        elif 'off' in line:
            turnoff(*num)
        elif "toggle" in line:
            toggle(*num)
    return int(lights.values.sum())

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
def day10_getNextValue(value):
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
        values.append(day10_getNextValue(values[i]))
    return len(values[-1])

def day10part2():
    values = ["3113322113"]
    times = 50 
    for i in range(times):
        values.append(day10_getNextValue(values[i]))
    return len(values[-1])

############################## Day 11 ##############################
def day11(mypassword):
    atoz = string.ascii_lowercase
    def base26todecimal(base26str):
        decimalValue = 0
        for i, v in enumerate(base26str):
            num = ord(v)-97 # a is 0, z is 25
            position = len(base26str)-i-1
            decimalValue += num*(26**position)
        return decimalValue
    def decimaltobase26(number):
        base26value = ""
        while number != 0:
            number , i = divmod(number, 26)
            base26value = atoz[i]+base26value
        return base26value
    def increase(mystr):
        # transfer to demimal value to perform add 
        decimalValue = base26todecimal(mystr)
        newDemcimalValue = decimalValue+1
        nextValue = decimaltobase26(newDemcimalValue)
        return nextValue
    # generate consecurtive 3 letters
    def generateThreeLetters():
        results = []
        for i in range(24):
            results.append(atoz[i]+atoz[i+1]+atoz[i+2])
        return results
    # check if match the criteria
    def isMatch(mystr):
        j = False
        # check if these element exit, easy to retur false if exits
        if any(el in mystr for el in ["i", "o", "l"]): 
            return j
        # check if double letter have 2 sets
        matchRepeat = re.findall(r'([a-z])\1{1}', mystr)
        if len(matchRepeat) < 2 :
            return j
        # check three consecutive letters
        threeLetter = generateThreeLetters()
        for el in threeLetter:
            if bool(re.search(el, mystr)):
                j = True
        return j

    s = False
    while not s:
        mypassword = increase(mypassword)
        s = isMatch(mypassword)
    return mypassword

def day11part1():
    return day11("hepxcrrq")

def day11part2():
    return day11(day11part1())


############################## Day 12 ##############################
def day12part1():
    mystr = read_file('12','string')
    myNumberList = re.findall(r'-?\d+', mystr) # optional - using ? in regex
    result = sum(list(map(lambda x: int(x), myNumberList)))
    return result

def day12part2():
    
    def getRedList(func):
        myRedList = []
        def wrapper(*arg):
            for i in func(*arg):
                myRedList.append(i)
            return myRedList
        return wrapper

    @getRedList
    def sortLastDictWithRed(startDict):
        if "red" in startDict.values():
            # myRedList.append(startDict)
            yield startDict
        else:
            for value in startDict.values():
                if isinstance(value,dict):
                    sortLastDictWithRed(value)
                elif isinstance(value,list): # explore down a layer if a list
                    for el in value:
                        if isinstance(el, dict):
                            sortLastDictWithRed(el)
                        elif isinstance(el, list):
                            mydict = {"mydict":el}
                            sortLastDictWithRed(mydict) # make sure recursion keeps going when list exist, explore down a layer if a list 
    
    mystr = read_file('12','string')
    myNumberList = re.findall(r'-?\d+', mystr) # optional - using ? in regex
    totolResult = sum(list(map(lambda x: int(x), myNumberList)))
    # get the list with red in dict as required
    myjsonDict = json.loads(mystr)
    # myRedList = getRedList(myjsonDict)
    myRedList = sortLastDictWithRed(myjsonDict)
    # find the number of within the red dicts
    myRedNumberList = re.findall(r'-?\d+', str(myRedList))
    redResult = sum(list(map(int, myRedNumberList)))
    # calculate final result
    return totolResult - redResult


############################## Day 13 ##############################
def day13part1():
    def getNeighbourHappiness():
        HappinessPoints = []
        Names = []
        mylist = read_file('13','list')
        for line in mylist:
            linelist = line.rstrip(".").split()
            HappinessPoints.append([linelist[0], linelist[-1], int(linelist[3])]) if linelist[2]=="gain" else HappinessPoints.append([linelist[0], linelist[-1], int(linelist[3])*-1])
            Names.append(linelist[0])
            NameList = list(set(Names))
        # print(HappinessPoints, NameList)
        return HappinessPoints, NameList
    
    # calculate each sitting happiness 
    def calculatePoints(sitting, HappinessPoints):
        points = 0
        for i in range(len(sitting)-1):
            for HP in HappinessPoints:
                if sitting[i] in HP and sitting[i+1] in HP:
                    points += HP[2]
        return points

    results =[]
    HappinessPoints, NameList = getNeighbourHappiness()
    # create all name list permutations to use to iterate
    allPermutations = list(itertools.permutations(NameList))
    # calculate points and push to results list
    for sitting in allPermutations:
        sittingAround = list(sitting)
        sittingAround.append(sitting[0])
        results.append(calculatePoints(sittingAround, HappinessPoints))
    # get the max value 
    return max(results)

def day13part2():
    def getNeighbourHappiness():
        HappinessPoints = []
        Names = []
        mylist = read_file('13','list')
        for line in mylist:
            linelist = line.rstrip(".").split()
            HappinessPoints.append([linelist[0], linelist[-1], int(linelist[3])]) if linelist[2]=="gain" else HappinessPoints.append([linelist[0], linelist[-1], int(linelist[3])*-1])
            Names.append(linelist[0])
            NameList = list(set(Names))
        # print(HappinessPoints, NameList)
        return HappinessPoints, NameList
        
    # calculate each sitting happiness 
    def calculatePoints(sitting, HappinessPoints):
        points = []
        for i in range(len(sitting)-1):
            neighbourPoint = []
            for HP in HappinessPoints:
                if sitting[i] in HP and sitting[i+1] in HP:
                    neighbourPoint.append(HP[2])
            points.append(sum(neighbourPoint))
        originalPoints = sum(points)
        
        # get the new points when include myself, to remove the samllest impact neighbore point effect
        points.sort(reverse=True)
        points.pop()
        # print(sum(points), originalPoints)
        return sum(points), originalPoints

    resultsNew = []
    resultsOriginal = []
    HappinessPoints, NameList = getNeighbourHappiness()
    # create all name list permutations to use to iterate
    allPermutations = list(itertools.permutations(NameList))

    # calculate points and push to results list
    for sitting in allPermutations:
        sittingAround = list(sitting)
        sittingAround.append(sitting[0])
        newPoints, originalPoints = calculatePoints(sittingAround, HappinessPoints)
        resultsNew.append(newPoints)
        resultsOriginal.append(originalPoints)
    # print("highest point for each case: ", max(resultsNew), max(resultsOriginal))
    return max(resultsNew)
############################## Day 14 ##############################
def day14part1():
    def get_parameter_list(mylist: list):
        fly_patthern = []
        for el in mylist:
            each = el.rstrip().split(" ")
            fly_patthern.append([int(each[3]), int(each[6]), int(each[-2])])
        return fly_patthern

    def get_distance(race_seconds: int, fly_pattern: list):
        cycle_seconds = fly_pattern[1] + fly_pattern[2]
        cycle_distance = fly_pattern[0] * fly_pattern[1]
        total_cycle, remains =  divmod(race_seconds, cycle_seconds)
        if remains < fly_pattern[1]:
            total_distance = cycle_distance * total_cycle + fly_pattern[0] * remains
        else:
            total_distance = cycle_distance * (total_cycle + 1)
        return total_distance

    race_seconds = 2503
    start = read_file("14", "list")
    results = []
    fly_pattern_list = get_parameter_list(start)
    for fly_pattern in fly_pattern_list:
        r = get_distance(race_seconds, fly_pattern)
        results.append(r)
    result = max(results)
    return result

def day14part2():
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
        winner_name = [key for key, value in winner_names.items() if value == max(winner_names.values())]
        return winner_name[0]
    
    totol_seconds = 2503
    start = read_file("14", "list")
    winner_name_scoreboard = {}
    for i in range(totol_seconds):
        winner = get_name(i+1)
        if winner in winner_name_scoreboard:
            winner_name_scoreboard[winner] += 1  
        else:
            winner_name_scoreboard[winner] = 1
    return max(winner_name_scoreboard.values())

############################## Day 15 ##############################
def get_parameter_list(mylist: list):
    parameters = []
    for el in mylist:
        numbers = re.findall(r'-?\d+', el)
        parameters.append(list(map(lambda el: int(el), numbers)))
    return parameters

def day15part1():
    start_list = read_file("15", "list")

    def cal_score(parameters: list, recipe: list):
        total_score = 0
        # get the property to iterate first, for exmaple capcity as the first i, leave the calories
        properties = len(parameters[0]) - 1
        total_score = 1
        for i in range(properties):
            property_score = 0
            for j in range(len(recipe)):
                property_score += parameters[j][i] * recipe[j]
            if property_score < 0:
                property_score = 0
            total_score *= property_score
        return total_score

    def cal_recipi_combination_score(parameters):
        # the ingredients type is 4, so the recipe here is 4, so to for loop 4 times
        for i in range(101):
            for j in range(101-i):
                for k in range(101-i-j):
                    for l in range(101-i-j-k):
                        recipe = [i, j, k, l]
                        recipe_score = cal_score(parameters, recipe)
                        yield recipe_score
    
    parameters = get_parameter_list(start_list)
    final_score = cal_recipi_combination_score(parameters)
    highest_score = max(final_score)
    return highest_score

def day15part2():
    start_list = read_file("15", "list")

    def cal_score_with_calories(parameters: list, recipe: list):
        total_score = 0
        # get the property to iterate first, for exmaple capcity as the first i, leave the calories
        properties = len(parameters[0]) - 1
        total_score = 1
        for i in range(properties):
            property_score = 0
            calories_score = 0
            for j in range(len(recipe)):
                property_score += parameters[j][i] * recipe[j]
                calories_score += parameters[j][len(parameters[0]) - 1] * recipe[j]
            if property_score < 0:
                property_score = 0
            elif calories_score != 500:
                property_score = 0
            total_score *= property_score
        return total_score

    def cal_recipi_combination_score(parameters):
        # the ingredients type is 4, so the recipe here is 4, so to for loop 4 times
        for i in range(101):
            for j in range(101-i):
                for k in range(101-i-j):
                    for l in range(101-i-j-k):
                        recipe = [i, j, k, l]
                        recipe_score = cal_score_with_calories(parameters, recipe)
                        yield recipe_score

    parameters = get_parameter_list(start_list)
    final_score = cal_recipi_combination_score(parameters)
    highest_score = max(final_score)
    return highest_score
############################## Day 16 ##############################
def day16part1():
    start_list = read_file("16", "list")
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

    one_message = {}
    for k, v in message.items():
        one_message[k] = str(v)

    for line in start_list:
        mylist = re.split(": |, ", line)
        it = iter(mylist[1:])
        rec_dict = dict(zip(it, it))
        if rec_dict.items() <= one_message.items():
            return line.split(" ")[1]

def day16part2():
    start_list = read_file("16", "list")
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
    for line in start_list:
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
            return line.split(" ")[1]

############################## Day 17 ##############################
def get_max_min(num_list):
    num_list.sort()
    for i in range(len(num_list)):
        if sum(num_list[:i+1]) == 150:
            max_n = i+1
            break
        elif sum(num_list[:i+1]) > 150:
            max_n = i
            break
    num_list.sort(reverse=True)
    for i in range(len(num_list)):
        if sum(num_list[:i+1]) >= 150:
            min_n = i+1
            break
    return max_n, min_n

def day17part1():
    START_LIST = read_file("17", "list")
    """main function"""
    result = 0
    num_list = [int(i) for i in START_LIST]
    max_n, min_n = get_max_min(num_list)
    for i in range(min_n, max_n+1):
        combination = itertools.combinations(num_list, i)
        for j in combination:
            # print(f"i is {i}, j is {j} sum is {sum(j)}")
            if sum(j) == 150:
                result += 1
    return result

def day17part2():
    START_LIST = read_file("17", "list")
    result = 0
    num_list = [int(i) for i in START_LIST]
    max_n, min_n = get_max_min(num_list)
    combination = itertools.combinations(num_list, min_n)
    for j in combination:
        if sum(j) == 150:
            result += 1
    return result

############################## Day 18 ##############################
def data_transform_18(data_input):
    a = list(map(lambda el: list(map(lambda el: 1 if el == "#" else 0, el)), data_input))
    all_zero = [0 for i in range(100)]
    b = [all_zero, *a, all_zero]
    c = list(map(lambda el: [0, *el, 0], b))
    return c

def cal_one_round(data):
    result = [a[:] for a in data]
    # need to break 2 layers
    # need to break the result to the elemental layer, otherwise the calculation cannot work
    # is only break one layer like result = data[:], then list of result[0] and data[0] is pointing to the same list
    # can use the id to check this, so every time data[i][j] change, result[i][j] also change

    # can uncomment the following 3 lines to check this one, check the id
    # result = data[:]
    # print(id(result[0]))
    # print(id(data[0]))

    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            if data[i][j] == 1 and check_neighbour_18(data, i, j, "on"):
                # print(data[i][j])
                # print(result[i][j])
                result[i][j] = 0 
                # print(data[i][j])
                # print(result[i][j])
            elif data[i][j] == 0 and check_neighbour_18(data, i, j, "off"):
                result[i][j] = 1
    return result

def check_neighbour_18(data, i, j, condition):
    sum_all = 0
    for a in range(i-1, i+2):
        for b in range(j-1, j+2):
            sum_all += data[a][b]
    if (condition == "on" and sum_all not in (3, 4)) or (condition == "off" and (sum_all == 3)):
        return True
    return False

def day18part1():
    START_LIST = read_file("18", "list")
    ready_data = data_transform_18(START_LIST)
    for i in range(100):
        ready_data = cal_one_round(ready_data)
    result = sum(map(sum, ready_data))
    return result

def day18part2():
    START_LIST = read_file("18", "list")

    def cal_one_round_two(data):
        result = [a[:] for a in data]
        for i in range(1, len(data)-1):
            for j in range(1, len(data[0])-1):
                if data[i][j] == 1 and check_neighbour_18(data, i, j, "on"):
                    if (i,j) not in [(1,1), (1,100), (100,1), (100,100)]:
                        result[i][j] = 0 
                elif data[i][j] == 0 and check_neighbour_18(data, i, j, "off"):
                    result[i][j] = 1
        return result

    ready_data = data_transform_18(START_LIST)
    ready_data[1][1] = ready_data[1][100]=ready_data[100][1]=ready_data[100][100]=1
    for i in range(100):
        ready_data = cal_one_round_two(ready_data)
    result = sum(map(sum, ready_data))
    return result

############################## Day 19 ##############################

def day19part1():
    START_LIST = read_file("19", "list")
    START_MOLECULE = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
    results = set()
    for i, v in enumerate(START_LIST):
        reaction = v.split(" => ")
        mol_list = START_MOLECULE.split(reaction[0])
        if len(mol_list) > 1:
            for j, k in enumerate(mol_list):
                if j < len(mol_list)-1:
                    a = reaction[0].join(mol_list[:j+1])
                    b = reaction[0].join(mol_list[j+1:])
                    new = [a, reaction[1], b]
                    results.add("".join(new))
        else:
            continue
    return(len(results))

def day19part2():
    START_LIST = read_file("19", "list")
    START_MOLECULE = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
    '''
    General rule
    Notice there are some element that does not iterate further with reaction
    So every time this element show 1 time, the reaction run 1 time
    '''
    # find all the elemnt and the length of all the final modecule
    el_all = re.findall(r"[A-Z][a-z]*", START_MOLECULE)
    el_all_set = set(el_all)
    # print(el_all)
    # print(len(el_all))

    # find el that can do further reactions
    reaction_variables = set(map(lambda el: el.split(" ")[0], START_LIST))
    # print(reaction_variables)

    # find el that cannot do further reactions
    el_no_reaction = el_all_set - reaction_variables
    # print(el_no_reaction)

    # put these element in a list and find their appearance time in the molecule
    counter = {el:el_all.count(el) for el in el_no_reaction}
    values = sorted(set(counter.values()))
    # print(counter, values)  # the result is {'Rn': 31, 'C': 1, 'Ar': 31, 'Y': 8}

    # now, eye ball analysis
    # for the 4 types Rn, C, Ar, Y, everytime there is Rn and Ar come, with C and Y
    # so must be Rn times reaction happen to get here
    # no_reaction_el_step_count = counter["Rn"]
    no_reaction_el_step_count = values[-1]
    # print(no_reaction_el_step_count)

    # with this Rn type of reaction, no reaction element(the 4 elements) should add this much length to the final module
    no_reaction_el_increase = sum(counter.values())
    # print(no_reaction_el_increase)

    # addtionally, every time Rn is there, the variable element + 1
    # every time Y is there, the varialbe element + 1
    # every time C is there, the varialbe does not change quantity, and reduce once the Rn adding
    # so the overall variable add by reaction wiht no_reaction elemenet is this
    # replace C with any possible value
    no_reaction_el_increase_variable = values[-1] + values[1] - values[0]
    
    # the variable_self_add is added by normal reaction, where 1 change to 2, so every reaction element increase 1 in the molecule
    variable_self_add = len(el_all) - no_reaction_el_increase - no_reaction_el_increase_variable
    # print(variable_self_add)

    # the reaction time happend within reactive variables self iteration
    variable_self_add_time = variable_self_add - 1 

    # final count how many times reaction happened
    result = variable_self_add_time + no_reaction_el_step_count
    # print(variable_self_add_time + no_reaction_el_step_count)
    return result

############################## Day 20 ##############################
def get_prime_factor_list(start, house_number):
    # get all the prime factors, meaning to break as small as possible
    prime_factor_list = []
    def get_prime_factor(start, house_number):
        for i in range(start, (house_number//start)+1):
            if house_number % i == 0:
                prime_factor_list.append(i)
                get_prime_factor(i, house_number//i)
                break
        prime_factor_list.append(house_number)
    get_prime_factor(start, house_number)
    return prime_factor_list[:(len(prime_factor_list)//2+1)]

def cal_all_combination_factors(factor_list):
    # from the prime factors, get all the factors 
    r = [i for i in factor_list]
    for k in range(2, len(factor_list)+1):
        combination = itertools.combinations(factor_list, k)
        for i in combination:
            b =  reduce(lambda x, y: x*y, i)   
            r.append(b)
    return list(set(r))

def day20part1():
    limit = 29000000
    # the number must have factor of 2 and 3, all prime number is 6n+1 or 6n-1
    for i in range(6,2900000,6):
        prime_factor_list = get_prime_factor_list(2, i)
        # print("prime factor list", prime_factor_list)
        if len(prime_factor_list) == 1:
            pass
        else:
            value = sum(cal_all_combination_factors(prime_factor_list))
            if value*10>limit:
                return i

def day20part2():
    limit = 29000000
    # the number must have factor of 2 and 3, all prime number is 6n+1 or 6n-1
    for i in range(6,2900000,6):
        prime_factor_list = get_prime_factor_list(2, i)
        # print("prime factor list", prime_factor_list)
        if len(prime_factor_list) == 1:
            pass
        else:
            combination_list = cal_all_combination_factors(prime_factor_list)
            # remove those less than 50 times, then to get the remaining
            gift_combination_list = filter(lambda x: x*50>=i, combination_list)
            value = sum(gift_combination_list)
            if value*11>limit:
                return i

############################## Day 21 ##############################
def day21():
    # define boss and player
    Profile = collections.namedtuple("Profile", ["HP", "Damage", "Armor"])
    boss = Profile(104, 8, 1)
    player_damage, player_armor  = 0, 0

    # define items to choose
    Items = collections.namedtuple("Items", "Cost, Damage, Armor")
    Weapons = list(map(Items._make, [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]))
    # add no choose condition as [0, 0, 0]
    Armors = list(map(Items._make, [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5], [0, 0, 0]])) 
    Rings = list(map(Items._make, [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3], [0, 0, 0]]))

    total_cost_win = []
    total_cost_lose = []
    # player equip situations evaluation to if win
    for w, a, r1, r2 in itertools.product(Weapons, Armors, Rings, Rings):
        if r1.Cost != r2.Cost or r1.Cost == 0 or r2.Cost == 0:
            player_damage = w.Damage+a.Damage+r1.Damage+r2.Damage
            player_armor = w.Armor+a.Armor+r1.Armor+r2.Armor
            # evaluate winning situation, considering player attack first
            boss_drop = max(1,player_damage-boss.Armor)
            player_drop = max(1, boss.Damage-player_armor)
            # win conditions
            if boss_drop > player_drop:
                total_cost_win.append(w.Cost+a.Cost+r1.Cost+r2.Cost) 
            # as player attack first
            elif boss_drop == player_drop and 100%boss_drop != 0 and boss_drop-(100%boss_drop)>=4:
                total_cost_win.append(w.Cost+a.Cost+r1.Cost+r2.Cost) 
            else: 
                total_cost_lose.append(w.Cost+a.Cost+r1.Cost+r2.Cost)
    return min(total_cost_win), max(total_cost_lose)

def day21part1():
    return day21()[0]


def day21part2():
    return day21()[1]

############################## Day 22 ##############################
def day22(mode):

    class Boss:
        def __init__(self, hp, damage, poison_timer):
            self.hp = hp
            self.damage = damage
            self.poison_timer = poison_timer
    boss = Boss(51, 9, 0)
    
    class Player: 
        def __init__(self, hp, mana, armor, shield_timer, recharge_timer):
            self.hp = hp
            self.mana = mana
            self.armor = armor
            self.shield_timer = shield_timer
            self.recharge_timer = recharge_timer
    player = Player(50, 500, 0, 0, 0)
    
    class Drug:
        def __init__(self, missile, drain, shield, poison, recharge):
            self.missile = missile
            self.drain = drain
            self.shield = shield
            self.poison = poison
            self.recharge = recharge
    cost_of_drugs = Drug(53, 73, 113, 173, 229)
    drugs_on_shelf = Drug(1, 1, 1, 1, 1)

    mana_usage = []
    
    # to clear the starting turn states
    def start_turn():
        if boss.poison_timer > 1:
            boss.hp -= 3
            boss.poison_timer -= 1
        elif boss.poison_timer == 1:
            boss.hp -= 3
            boss.poison_timer -= 1
            drugs_on_shelf.poison = 1

        if player.shield_timer > 1:
            player.armor = 7
            player.shield_timer -= 1
        elif player.shield_timer == 1:
            player.shield_timer -= 1
            drugs_on_shelf.shield = 1
            player.armor = 0

        if player.recharge_timer > 1:
            player.mana += 101
            player.recharge_timer -= 1
        elif player.recharge_timer == 1:
            player.mana += 101
            player.recharge_timer -= 1
            drugs_on_shelf.recharge = 1

    def evaluate_win():
        if boss.hp <= 0:
            print("player win") 
            return mana_usage
        elif player.mana < 0 or player.hp <= 0:
            print("boss win")
            return mana_usage
    
    def use_missile():
        player.mana -= cost_of_drugs.missile
        mana_usage.append(cost_of_drugs.missile)
        boss.hp -= 4
    
    def use_drain():
        boss.hp -= 2
        player.hp += 2
        player.mana -= cost_of_drugs.drain
        mana_usage.append(cost_of_drugs.drain)
    
    def use_recharge():
        player.mana -= cost_of_drugs.recharge
        mana_usage.append(cost_of_drugs.recharge)
        player.recharge_timer = 5
        drugs_on_shelf.recharge = 0

    def use_poison():
        player.mana -= cost_of_drugs.poison
        mana_usage.append(cost_of_drugs.poison)
        boss.poison_timer = 6
        drugs_on_shelf.poison = 0

    def use_shield():
        player.mana -= cost_of_drugs.shield
        mana_usage.append(cost_of_drugs.shield)
        player.shield_timer = 6     
        drugs_on_shelf.shield = 0

    def player_make_choice(mode):
        # calcuate when to use missile to finish the boss
        # 2 * player.shield_timer / 2 + 9 * (player_turn_to_death-player.shield_timer) / 2 + player_turn_to_death / 2 < player.hp
        # boss.poison_timer * 3 + boss_turn_to_death_fastest // 2 * 4 > boss.hp
        if mode == "hard":
            player_turn_to_death = (player.hp + 3.5 * player.shield_timer) // 5 + 1
        else:
            player_turn_to_death = (player.hp + 3.5 * player.shield_timer) // 4.5 + 1
        boss_turn_to_death_fastest = (boss.hp - boss.poison_timer * 3) // 2 

        if boss_turn_to_death_fastest < player_turn_to_death and player.mana >= player_turn_to_death * cost_of_drugs.missile // 2 :
            use_missile()
            print("attack to the end with missile")
        # use drain to make a difference on the turn to death, because the hard model only lost on the extra 1 point, so need one drain to make a difference
        elif boss_turn_to_death_fastest == player_turn_to_death and player.mana >= player_turn_to_death * cost_of_drugs.missile // 2 :
            use_drain()
        elif drugs_on_shelf.recharge == 1 and player.mana >= cost_of_drugs.recharge and player.mana <= cost_of_drugs.recharge + cost_of_drugs.poison:
            use_recharge()
        elif drugs_on_shelf.poison == 1 and player.mana >= cost_of_drugs.shield:
            use_poison()
        elif drugs_on_shelf.shield == 1 and player.mana >= cost_of_drugs.shield:
            use_shield()
        else:
            use_drain()
    
    def boss_attack():
        attack_force = boss.damage - player.armor
        player.hp -= max(1, attack_force)

    # max 500 turn surely finished
    for i in range(500):
        if mode == "hard":
            player.hp -= 1
        if evaluate_win():
            print("end with round ", i)
            print(mana_usage)
            result = evaluate_win()
            return sum(result)
        start_turn()
        if evaluate_win():
            print("end with round ", i)
            print(mana_usage)
            result = evaluate_win()
            return sum(result)
        if mode == "hard":
            player_make_choice("hard")
        else: 
            player_make_choice("easy")
        start_turn()
        boss_attack()
        if evaluate_win():
            print("end with rount ", i)
            print(mana_usage)
            result = evaluate_win()
            return sum(result)
        # print("player hp", player.hp)
        # print("player mana", player.mana)
        # print("boss hp", boss.hp)
        # print("")

def day22part1():
    return day22("easy")

def day22part2():
    return day22("hard")


if __name__ == "__main__": print(day22part1())














