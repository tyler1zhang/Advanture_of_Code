
def main():
    import re
    from functools import reduce

    # read file and split to lines in a list
    with open('input') as f:
        mylist = f.read().splitlines() 

    def isNice(eachstr):
        # use regex to construct the pattern
        repeatpattern = re.compile(r"([a-z][a-z]).*\1")
        repeat = repeatpattern.search(eachstr)

        # use regex to construct the pattern
        sandwichpattern = re.compile(r"([a-z]).\1")
        sandwich = sandwichpattern.search(eachstr)

        # return 1 if it meets nice criteria
        if repeat and sandwich  :
            return 1
        else:
            return 0

    result = reduce(lambda a,b: a+b, list(map(isNice, mylist)))
    print(result)

    f.close()

if __name__ == '__main__': main()
