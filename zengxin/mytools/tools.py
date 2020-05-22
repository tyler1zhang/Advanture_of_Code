
import time
def read_file(type):
    with open('input') as f:
        if type == "line":
            mylist = f.read().splitlines() 
            
        elif type == "string":
            mystring = f.read()
    f.close()
    return mylist if mylist else mystring

def get_time(f):
    def cal_time():
        start_time = time.time()
        f()
        print(time.time() - start_time)
    return cal_time