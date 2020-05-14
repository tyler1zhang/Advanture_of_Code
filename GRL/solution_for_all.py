import requests
from pycookiecheat import chrome_cookies #pip3 install pycookiecheat

###########  Global Function  #############

#To retrieve question input with param: year and question number
#To invoke this function, login onto Github with chrome is a must 
def get_input(question_num, year='2015'):
    input_url='https://adventofcode.com/'+year+'/day/'+question_num+'/input'
    cookies = chrome_cookies(input_url)    
    content = requests.get(input_url, cookies=cookies).text
    return content

###########  Starting of Solution  #############

def q1_2015_part1():
    '''
        An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
        The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.   
        For example:   
        (()) and ()() both result in floor 0.
        ((( and (()(()( both result in floor 3.
        ))((((( also results in floor 3.
        ()) and ))( both result in floor -1 (the first basement level).
        ))) and )())()) both result in floor -3.
        To what floor do the instructions take Santa?
    '''
    input=get_input('1','2015')
    answer= input.count('(')-input.count(')')
    return answer

def q1_2015_part2():
    '''
        Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). 
        The first character in the instructions has position 1, the second character has position 2, and so on.
    '''
    input=get_input('1','2015')
    for index in range(len(input)):
        current_floor=input.count('(',0,index)-input.count(')',0,index)
        #print(index, current_floor)
        if current_floor==-1:
            return index
        
def q2_2015_part1():
    '''
        Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper 
        for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little 
        extra paper for each present: the area of the smallest side.
        All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
    '''
    input=get_input('2','2015').splitlines()
    total_area=0
    for item in input:
        side=item.split('x')
        side=[int(side[0]),int(side[1]),int(side[2])]
        area1=side[0]*side[1]
        area2=side[0]*side[2]
        area3=side[1]*side[2]
        smallest_area=min(area1, area2, area3)
        total_area+=2*(area1+area2+area3)+smallest_area
        
    return total_area

def q2_2015_part2():
    '''
        The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. 
        Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to 
        the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.
        How many total feet of ribbon should they order?
    '''
    input=get_input('2','2015').splitlines()
    total_area=0
    for item in input:
        side=item.split('x')
        side=[int(side[0]),int(side[1]),int(side[2])]
        largest_side=max(side[0], side[1], side[2])

        total_area+=2*(side[0]+side[1]+side[2])-2*largest_side+side[0]*side[1]*side[2]
        
    return total_area

def q3_2015_part1():
    '''
        Santa is delivering presents to an infinite two-dimensional grid of houses.He begins by delivering a present to the house at 
        his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are 
        always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present 
        to the house at his new location.
    
        However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa 
        ends up visiting some houses more than once. How many houses receive at least one present?
    '''
    input=get_input('3','2015')
    coordinate_set={'0/0',}
    current_x=0
    current_y=0
    for char in input:
        if char=='^':
            current_y+=1
        elif char=='v':
            current_y-=1
        elif char=='<':
            current_x-=1
        elif char=='>':
            current_x+=1
        coordinate_set.add(str(current_x)+'/'+str(current_y))
    
    return len(coordinate_set)

def q3_2015_part2():
    '''
        Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving 
        based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
        
        This year, how many houses receive at least one present?
    '''
    input=get_input('3','2015')
    coordinate_set={'0/0',}
    santa_x=0
    santa_y=0
    robo_x=0
    robo_y=0
    santa_to_move=True
    
    for char in input:
        if santa_to_move:
            if char=='^':
                santa_y+=1
            elif char=='v':
                santa_y-=1
            elif char=='<':
                santa_x-=1
            elif char=='>':
                santa_x+=1
            coordinate_set.add(str(santa_x)+'/'+str(santa_y))
        else: 
            if char=='^':
                robo_y+=1
            elif char=='v':
                robo_y-=1
            elif char=='<':
                robo_x-=1
            elif char=='>':
                robo_x+=1
            coordinate_set.add(str(robo_x)+'/'+str(robo_y))
        #change turn    
        santa_to_move=not santa_to_move
        
    return len(coordinate_set)            
            
###########  Execution  #############
print(q3_2015_part2())