from functools import reduce

def main():

    f = open('input', 'r')
    boxs = tuple(f.readlines())
    results=[]
    
    for box in boxs:
        boxspec=box.rstrip().split("x")
        boxspecint=list(map(int, boxspec))
        boxspecint.sort()

        ribbonwrap=(boxspecint[0]+boxspecint[1])*2
        ribbonbowl=reduce((lambda x, y: x *y), boxspecint)
        ribbonall=ribbonwrap+ribbonbowl
        # get individual result
        results.append(ribbonall)
    #get final results
    calnum=reduce((lambda x,y:x+y), results)
    print(calnum)
    
    f.close()

if __name__ == '__main__': main()