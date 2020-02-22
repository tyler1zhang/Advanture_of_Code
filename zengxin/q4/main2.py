def main():
    import hashlib
    
    f = open('input', 'r')
    initValue = f.read().rstrip()
    restValue = 254575
    goal = False
    while goal != True:

        result = initValue + str(restValue)
        h = hashlib.md5(result.encode())
        hexvalue = h.hexdigest()
        goal = True if hexvalue[0:6] == "000000" else False
        restValue += 1
        # print(result)
        
        # add a stopper not running to much
        if restValue > 3000000:
            break
    if goal:
        print(f"the result is {result}")
    f.close()

if __name__ == '__main__': main()