# a is 97, z is 122 for ord
# ref: https://stackoverflow.com/questions/1181919/python-base-36-encoding

import re
import string

# generate string a to z
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
    # print(base26value)
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

def main():
    s = False
    mypassword = "hepxcrrq" # question 1
    mypassword = "hepxxyzz" # question 2
    while not s:
        mypassword = increase(mypassword)
        s = isMatch(mypassword)
    print("the answer is ", mypassword)

main()