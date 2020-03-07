#!/usr/bin/evn python

from functools import reduce

# 0 to 9 list
mylist= range(0,10)

mymaplist = list(map(lambda x: x*2,mylist))
print(mymaplist)

myreduce = reduce((lambda a, b: a+b), mymaplist)
print(myreduce)


# losing map, map cannto be used 2nd time, why?
a = range(1,10)
mymap = map(lambda x: x*x, a)
list1 = list(mymap)
list2 = list(mymap)

print(f'my list1 is {list1}')
print(f'my list2 is {list2}')