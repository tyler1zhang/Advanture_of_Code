
def main():

    f = open('input', 'r')
    allarrows = f.read()
    x = 0
    y = 0
    origin = [(x,y)]
    for i in allarrows:
        if i == ">":
            x += 1
        elif i =="<":
            x -= 1
        elif i == "^":
            y += 1
        elif i == "v":
            y -= 1
        origin.append((x,y))
    uniquevalue = list(set(origin))
    print(len(uniquevalue))
    
    f.close()

if __name__ == '__main__': main()
