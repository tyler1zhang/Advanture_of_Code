#!/usr/bin/env python

def read_file(type):
    with open('input') as f:
        if type == "line":
            mylist = f.read().splitlines() 
            
        elif type == "string":
            mystring = f.read()
    f.close()
    return mylist if mylist else mystring

'''
#!/usr/bin/env python
import sys
sys.path.append("..")
from mytools import tools

start_list = tools.read_file("line")


def main(input):

    result = 0
    print(result)
    return(result)

main(start_list)
'''