# -*- coding: utf-8 -*-
import csv

#### to write data to csv file####
def write_csv(file, fieldnames, data):
    
    with open(file, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        for row in data:
            writer.writerow(row)

file='GTZZ_Team.csv'
fieldnames = ['index', 'name', 'sex']        
data=[{'index': 1, 'name': 'Zeng Xin', 'sex': 'M'},
      {'index': 2, 'name': 'Zhang Tianliang', 'sex': 'M'},
      {'index': 3, 'name': 'Tao Sui', 'sex': 'M'},
      {'index': 4, 'name': 'Guo Ruiliang', 'sex': 'M'},
      ]
print(write_csv(file, fieldnames, data))