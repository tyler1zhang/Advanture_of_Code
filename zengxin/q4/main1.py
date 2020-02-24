
def main():
    import hashlib
    

    f = open('input', 'r')
    initValue = f.read().rstrip()
    restValue = 0
    goal = False
    while goal != True:
        # check if hash value match the 00000
        result = initValue + str(restValue)
        h = hashlib.md5(result.encode())
        hexvalue = h.hexdigest()
        goal = True if hexvalue[0:5] == "00000" else False
        restValue += 1
        
        # add a stopper not running to much
        if restValue > 3000000:
            break
    if goal:
        print(f"the result is {result}")
    f.close()

if __name__ == '__main__': main()