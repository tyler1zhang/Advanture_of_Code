import pandas as pd

sue_str = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''

# Get the input from file about 500 Aunt Sue
with open("./input/2015/q16.txt") as f:
    lst = f.read().splitlines()
f.close()

# Get the input from the Aunt Sue who sent you gift
aunt_sue_lst = sue_str.split()
aunt_sue_dic = {}
for i in range(0, len(aunt_sue_lst), 2):
    aunt_sue_dic.update([(aunt_sue_lst[i][:-1], int(aunt_sue_lst[i+1]))])

# headers is a list for column names
headers = ['Sue']
for k in aunt_sue_dic.keys():
    headers.append(k)

# Use input to generate the body of dataframe
data_lst = []
i = 1
for line in lst:
    t = line.split()
    data_lst.append({t[0]: i, t[2][:-1]:int(t[3][:-1]), 
                    t[4][:-1]: int(t[5][:-1]), t[6][:-1]: int(t[7])})
    i += 1

# For the items forgot, use the value -2 instead of NA in the df.
forgot_info = -2
df = pd.DataFrame(data = data_lst, columns = headers).fillna(forgot_info).astype('int32')

# Function return series of bool value, use
def check_item(name_str, v):
    return ((df[name_str] == v) | (df[name_str] == forgot_info))

# Below two funcations for Part 2
def check_item_greater(name_str, v):
    return ((df[name_str] > v) | (df[name_str] == forgot_info))

def check_item_fewer(name_str, v):
    return ((df[name_str] < v) | (df[name_str] == forgot_info))

bool_result_p1 = df['Sue'] > 0 
for k1, v1 in aunt_sue_dic.items():
    bool_result_p1 &= check_item(k1, v1)

bool_result_p2 = df['Sue'] > 0 
for k2, v2 in aunt_sue_dic.items():
    if k2 in ['cats', 'trees']:
        bool_result_p2 &= check_item_greater(k2, v2)
    elif k2 in ['pomeranians', 'goldfish']:
        bool_result_p2 &= check_item_fewer(k2, v2)
    else:
        bool_result_p2 &= check_item(k2, v2)


if __name__ == '__main__':
    print(f"Part 1 result is {int(df[bool_result_p1]['Sue'])}")
    print(f"Part 2 result is {int(df[bool_result_p2]['Sue'])}")
    #print(df.head())
