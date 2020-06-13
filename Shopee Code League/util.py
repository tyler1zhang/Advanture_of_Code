# -*- coding: utf-8 -*-
import csv

#### to read data from csv file####
def read_csv(file):
    with open(file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        print(f'field names are {csv_reader.fieldnames}')
        for row in csv_reader:
            print(row.values())
    
#### to write data to csv file####
def write_csv(file, fieldnames, data):
    
    with open(file, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        for row in data:
            writer.writerow(row)


### Testing ###  
file='GTZZ_Team.csv'
fieldnames = ['index', 'name', 'sex']        
data=[{'index': 1, 'name': 'Zeng Xin', 'sex': 'M'},
      {'index': 2, 'name': 'Zhang Tianliang', 'sex': 'M'},
      {'index': 3, 'name': 'Tao Sui', 'sex': 'M'},
      {'index': 4, 'name': 'Guo Ruiliang', 'sex': 'M'},
      ]
#write_csv(file, fieldnames, data)
read_csv(file)