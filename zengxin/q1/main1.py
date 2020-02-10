def main():

    f = open('input', 'r')
    floor = 0
    for i in f.read(): 
        if i == '(':
            floor += 1
        elif i ==')':
            floor -= 1
    print(floor)

# if __name__ == '__main__': main()
main()
'''
if I run main() directly, once it is imported by import.py, 
it will run automatically.
if I use the __name__ == '__main__' here, onc it is imported by import.py
it will not run, until it is called
'''