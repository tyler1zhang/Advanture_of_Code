# -*- coding: utf-8 -*-
import csv

#### to write data to csv file####
def write_csv(file, fieldnames, data):
    
    with open(file, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def solve_dummy_competition():
    file='competition_dummy.csv'
    fieldnames = ['id', 'new_number'] 
    data=[]
    for id in range(101):     
        data.append({'id': id, 'new_number': id+2})
    write_csv(file, fieldnames, data)
    print('solution exported to', file)

### execution ###    
solve_dummy_competition()