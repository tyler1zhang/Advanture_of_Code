def main():

    f = open('input', 'r')
    allarrows = f.read()
    # get each individual arrows
    santaarrows = allarrows[0:len(allarrows):2]
    robotarrows = allarrows[1:len(allarrows):2]

    # return each one list
    santalist = oneperson(santaarrows)
    robolist = oneperson(robotarrows)
    # add up to one list
    finallist = santalist + robolist

    # final unique list
    finaluniquelist = list(set(finallist))
    print(len(finaluniquelist))

    f.close()

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

if __name__ == '__main__': main()