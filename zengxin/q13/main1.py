# Travelling Salesperson Problems, only can solve to a small sets, otherwise too big to iterate
import time
import itertools
import sys
sys.path.append("..")
from mytools import tools

def getNeighbourHappiness():
    HappinessPoints = []
    Names = []
    with open('input') as f:
        mylist = f.read().splitlines() 
    f.close()
    for line in mylist:
        linelist = line.rstrip(".").split()
        HappinessPoints.append([linelist[0], linelist[-1], int(linelist[3])]) if linelist[2]=="gain" else HappinessPoints.append([linelist[0], linelist[-1], int(linelist[3])*-1])
        Names.append(linelist[0])
        NameList = list(set(Names))
    # print(HappinessPoints, NameList)
    return HappinessPoints, NameList
    
getNeighbourHappiness()

# calculate each sitting happiness 
def calculatePoints(sitting, HappinessPoints):
    points = 0
    for i in range(len(sitting)-1):
        for HP in HappinessPoints:
            if sitting[i] in HP and sitting[i+1] in HP:
                points += HP[2]
    return points

results =[]

@tools.get_time
def main():
    HappinessPoints, NameList = getNeighbourHappiness()

    # create all name list permutations to use to iterate
    allPermutations = list(itertools.permutations(NameList))
    print(allPermutations[0])
    print("overall permutation number:", len(allPermutations))

    # calculate points and push to results list
    for sitting in allPermutations:
        sittingAround = list(sitting)
        sittingAround.append(sitting[0])
        results.append(calculatePoints(sittingAround, HappinessPoints))
    print("overall result number: ", len(results))

    # get the max value 
    print("highest point is: ", max(results))


main()
