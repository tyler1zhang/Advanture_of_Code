import time

def read_file(num, _type):
    mylist=[]
    path = f"./input/input{num}"
    with open(path) as f:
        if _type == "string":
            mystring = f.read().rstrip()
        elif _type == "list":
            mylist = f.read().splitlines()
    f.close()
    return mylist if mylist else mystring

def get_time(f):
    def cal_time():
        start_time = time.time()
        f()
        print(time.time() - start_time)
    return cal_time