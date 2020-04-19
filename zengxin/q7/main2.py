## use regression to check through the whole doc again and again
## use dict to host the result
mydict = {}

# Function to rune the  calculation
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
    if varlast == "b":
        mydict["b"] = 956
        fulllist.remove(" ".join(linelist))
    if var1.isdigit() and varlast != "b":
        mydict[varlast] = int(var1)
        fulllist.remove(" ".join(linelist))
    elif var1 in mydict:
        mydict[varlast] = int(mydict[var1])
        fulllist.remove(" ".join(linelist))

def checkLogic(fulllist,count):
    # add a breaker to not go infinite loop, play with the number
    count += 1
    if count > 300: 
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

def main():
    # read file and split to lines in a list
    with open('input') as f:
        mylist = f.read().splitlines() 
    # for breaker
    count = 1
    checkLogic(mylist,count)
    f.close()

if __name__ == '__main__': main()
