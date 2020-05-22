
# look and say game https://www.youtube.com/watch?v=ea7lJkEhytA
import re

values = ["3113322113"]
times = 40 # question 1
times = 55 # question 2

def getNextValue(value):
    # separation by duplication
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

    # make to string and return 
    strResult = "".join(results)
    print(len(strResult))
    return strResult

def main():
    for i in range(times):
        values.append(getNextValue(values[i]))
import datetime
t1 = datetime.datetime.now()
main()
t2 = datetime.datetime.now()
print(t2-t1)