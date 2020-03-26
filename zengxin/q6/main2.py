import numpy as np
import pandas as pd
import re

# generate 2D array to map
# Ref: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-integer
lights = pd.DataFrame(0, range(0,1000), range(0,1000))

# Function to rune the  calculation
def turnon(x1,y1,x2,y2): 
    lights.loc[x1:x2,y1:y2] += 1

def turnoff(x1,y1,x2,y2):
    # use applymap to map individual cell
    lights.loc[x1:x2,y1:y2] = lights.loc[x1:x2,y1:y2].applymap(lambda x: x-1 if x > 0 else 0)

def toggle(x1,y1,x2,y2):
    lights.loc[x1:x2,y1:y2] += 2

def main():
    # read file and split to lines in a list
    with open('input') as f:
        mylist = f.read().splitlines() 

    for line in mylist:
        numstr = re.findall(r'\d+',line)
        num = list(map(lambda x: int(x),numstr)) # need to change to int otherwise has some parsing issue
        if 'on' in line:
            turnon(*num)
        elif 'off' in line:
            turnoff(*num)
        elif "toggle" in line:
            toggle(*num)
        
    print(f'the result is {lights.values.sum()}')
    f.close()

if __name__ == '__main__': main()
