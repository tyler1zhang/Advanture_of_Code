from functools import reduce

def main():

    f = open('input', 'r')
    boxs = tuple(f.readlines())
    results=[]
    
    for box in boxs:
        boxspec=box.rstrip().split("x")
        boxspecint=list(map(int, boxspec))

        allfaces=(boxspecint[0]*boxspecint[1]+boxspecint[0]*boxspecint[2]+boxspecint[1]*boxspecint[2])*2
        smallestface=min([boxspecint[0]*boxspecint[1], boxspecint[0]*boxspecint[2], boxspecint[1]*boxspecint[2]])
        # get individual result
        result=allfaces+smallestface
        results.append(result)
    #get final results
    calnum=reduce((lambda x,y:x+y), results)
    print(calnum)

    f.close()

if __name__ == '__main__': main()