#!/usr/bin/env node

myarray = [...Array(10).keys()]
map = myarray.map(el => el*2)
console.log(map)

mapreduce = myarray.map(el => el*2).reduce( (a,c) => a+c)
console.log(mapreduce)