def main():

    f = open('input', 'r')
    floor = 0
    list_floor = tuple(f.readlines()[0])
    
    for index, value in enumerate(list_floor): 
        if value == '(':
            floor += 1
        elif value ==')':
            floor -= 1
            if floor ==-1: print(index+1)

if __name__ == '__main__': main()