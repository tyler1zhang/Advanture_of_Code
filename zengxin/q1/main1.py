def main():

    f = open('input', 'r')
    floor = 0
    for i in f.read(): 
        if i == '(':
            floor += 1
        elif i ==')':
            floor -= 1
    print(floor)

if __name__ == '__main__': main()