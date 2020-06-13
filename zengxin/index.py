
from util import read_file
from functools import reduce
import hashlib
import string
import re
import pandas as pd
import itertools
import json

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
start = tools.read_file("line")

def get_parameter_list(mylist: list):
    fly_patthern = []
    for el in mylist:
        each = el.rstrip().split(" ")
        fly_patthern.append([int(each[3]), int(each[6]), int(each[-2])])
    print("fly patterns: ", fly_patthern)
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

def main(race_seconds: int):
    results = []
    fly_pattern_list = get_parameter_list(start)
    for fly_pattern in fly_pattern_list:
        r = get_distance(race_seconds, fly_pattern)
        results.append(r)
    result = max(results)
    print(result)
    return result

main(2503)



############################## Day 15 ##############################
############################## Day 16 ##############################
############################## Day 17 ##############################
############################## Day 18 ##############################
############################## Day 19 ##############################
############################## Day 20 ##############################

print(day13part2())
