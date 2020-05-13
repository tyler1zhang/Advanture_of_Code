import re
    
def main():
    with open('input.json') as f:
        mystr = f.read()
        myNumberList = re.findall(r'-?\d+', mystr) # optional - using ? in regex
        result = sum(list(map(lambda x: int(x), myNumberList)))
        print(result)
    f.close()

if __name__ == '__main__': main()