# Travelling Salesperson Problems, only can solve to a small sets, otherwise too big to iterate

import itertools

# create distance list to host the data, create all stations name host
def getDistanceList():
    distanceList = []
    Stations = []
    with open('input') as f:
        mylist = f.read().splitlines() 
        for line in mylist:
            linelist = line.rstrip().split()[::2]
            Stations.extend(linelist[:2])
            distanceList.append(linelist)
    f.close()
    allStations = list(set(Stations))
    return distanceList, allStations

# calculate each route distance from the distancelist data
def calculateDistance(route, distanceList):
    distanceValue = 0
    for i in range(len(route)-1):
        for distance in distanceList:
            if route[i] in distance and route[i+1] in distance:
                distanceValue += int(distance[2])
    return distanceValue

results =[]
def main():
    distanceList, allStations = getDistanceList()

    # create all stations permutations to use to iterate
    allPermutations = list(itertools.permutations(allStations))
    print("overall permutation number:", len(allPermutations))

    # calculate each distance and push to results list
    for route in allPermutations:
        results.append(calculateDistance(route, distanceList))
    print("overall result number: ", len(results))

    # get the min value 
    print("shortest route is: ", min(results))

# need to export results
main()