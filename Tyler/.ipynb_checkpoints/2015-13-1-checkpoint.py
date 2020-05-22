import itertools
import pandas as pd


# Shift one name and generate another tuple
def shift_tuple(t):
    lst = list(t)
    l1 = lst[1:]
    l1.append(lst[0])
    t1 = tuple(l1)
    return t1

# Based on name list to return all scenarios list. 
def scenarios_names(name_list):
    # Due to cycle table, every squence will be repeated by 2*len(s) times. ex: "abc" is same as "bca", "cab" and 3 reverse sequence. 
    permutations_list = list(itertools.permutations(name_list))
    
    all_scenarios_list = []
    sequence_tuple_set = {''}

    for line_tuple in permutations_list:
        if line_tuple not in sequence_tuple_set:
            all_scenarios_list.append(line_tuple)
        temp_lst = list(line_tuple)
        temp_lst.reverse()
        temp_tuple = tuple(temp_lst)
        temp_tuple_r = line_tuple
        i = len(line_tuple)
        while i >0:
            sequence_tuple_set.add(temp_tuple_r)
            sequence_tuple_set.add(temp_tuple)
            temp_tuple_r = shift_tuple(temp_tuple_r)
            temp_tuple = shift_tuple(temp_tuple)
            i -= 1
            
    return all_scenarios_list

# Use name sequence tuple and happiness data DF to get the sum happiness of one scenario. 
def cal_happiness(onetuple, one_df):
    result = 0
    num = len(onetuple)
    for i in range(-1, num-1):
        result += one_df[onetuple[i]][onetuple[i+1]] + one_df[onetuple[i+1]][onetuple[i]]
    return result    


# Execution 
if "__name__" == "__main__":
    # Read the data from input file. 
    with open('2015-Q13_tyler.txt') as f:
        data_lst = []
        names_lst = []
        for line in f.readlines():
            line_lst = line.split()
            if line_lst[2] == 'gain':
                data_lst.append([line_lst[0], int(line_lst[3]), line_lst[-1][:-1]])
            else:
                data_lst.append([line_lst[0], -int(line_lst[3]), line_lst[-1][:-1]])
            names_lst.append(line_lst[0])
        names_lst = set(names_lst)
    f.close()

    all_scenarios = scenarios_names(names_lst)

    df = pd.DataFrame(index = names_lst, columns = names_lst)
    for line in data_lst:
        df[line[0]][line[2]] = line[1]
    df.fillna(0)

    part1_results = []
    for t in all_scenarios:
        r = cal_happiness(t, df)
        part1_results.append(r)
    print(f'Max_happiness for part1 is {max(part1_results)}')
    

