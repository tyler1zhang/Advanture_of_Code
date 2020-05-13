import re
import json

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

def main():
    with open('input.json') as f:
        mystr = f.read()
    f.close()

    myNumberList = re.findall(r'-?\d+', mystr) # optional - using ? in regex
    totolResult = sum(list(map(lambda x: int(x), myNumberList)))

    # get the list with red in dict as required
    myjsonDict = json.loads(mystr)
    print(myjsonDict)
    # myRedList = getRedList(myjsonDict)
    myRedList = sortLastDictWithRed(myjsonDict)

    print("this is my red list ", myRedList)

    # find the number of within the red dicts
    myRedNumberList = re.findall(r'-?\d+', str(myRedList))
    redResult = sum(list(map(lambda x: int(x), myRedNumberList)))

    # calculate final result
    finalResult = totolResult - redResult
    print(totolResult, redResult, finalResult)

# at the beginning it is always wrong, so I try to use the output to make some compare then found out the list is not recursive to the end
if __name__ == '__main__': main()
