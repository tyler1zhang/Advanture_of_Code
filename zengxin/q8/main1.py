import re

def checkeachline(line):
    fulllength = len(line)
    # remove hex value
    hexvalue = re.findall(r'\\x[0-9,a-f][0-9,a-f]',line)
    if hexvalue:
        print("hex",hexvalue)
        for el in hexvalue:
            line = line.replace(el,'!')
    # remove bashslash \ value
    backslash = re.findall(r'\\.', line)
    if backslash:
        for el in backslash:
            line = line.replace(el,'~')
    # change the side double quote
    strlength = len(line)-2

    return (fulllength,strlength)
    
def main():
    # read file and split to lines in a list
    with open('input') as f:
        mylist = f.read().splitlines() 
    fulllength =[]
    strlength = []
    for line in mylist:
        result = checkeachline(line)
        fulllength.append(result[0])
        strlength.append(result[1])
    print(fulllength)
    print(f'the full length sum is {sum(fulllength)}')
    print(strlength)
    print(f'the string length sum is {sum(strlength)}')
    print(f'the result is {sum(fulllength)-sum(strlength)}')
    f.close()

if __name__ == '__main__': main()