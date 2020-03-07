
def main():
    import string
    from functools import reduce

    # get ready the starting double letter and sequence
    atoz = list(string.ascii_lowercase)
    listdouble = list(map(lambda el: el+el, atoz))
    listsequence =["ab", "cd", "pq", "xy"]

    # read file and split to lines in a list
    with open('input') as f:
        mylist = f.read().splitlines() 

    def isNice(eachstr):
        # check vowels count
        vowelsCount = list(filter(lambda x: x in ["a","e","i","o","u"], list(eachstr)))
        print(len(vowelsCount))

        # check if have double letter
        sameLetters = True if True in list(map(lambda x: x in eachstr, listdouble)) else False

        # check if have sequence letter
        sequenceletters = True if True in list(map(lambda x: x in eachstr, listsequence)) else False

        # return 1 if it meets nice criteria
        if len(vowelsCount)>2 and sameLetters and not sequenceletters :
            return 1
        else:
            return 0

    result = reduce(lambda a,b: a+b, list(map(isNice, mylist)))
    print(result)

    f.close()

if __name__ == '__main__': main()
