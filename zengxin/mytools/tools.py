#!/usr/bin/evn python

def read_file(type):
    with open('input') as f:
        if type == "line":
            mylist = f.read().splitlines() 
            
        elif type == "string":
            mystring = f.read()
    f.close()
    return mylist if mylist else mystring
