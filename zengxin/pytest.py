#!/usr/bin/evn python

from functools import reduce

# 0 to 9 list
mylist= range(0,10)

mymaplist = list(map(lambda x: x*2,mylist))
print(mymaplist)

myreduce = reduce((lambda a, b: a+b), mymaplist)
print(myreduce)
