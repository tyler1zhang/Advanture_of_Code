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
        newPoints, originalPoints = calculatePoints(sittingAround, HappinessPoints)
        resultsNew.append(newPoints)
        resultsOriginal.append(originalPoints)

    # get the max value 
    print("highest point for each case: ", max(resultsNew), max(resultsOriginal))

# start_time = time.time()
# main()
# print(time.time() - start_time)

main()