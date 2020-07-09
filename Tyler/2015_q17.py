def get_target_value(lst, target):
    """
    Output a list which sum of number higher than target value
    """
    take_number = []
    total = 0
    for c in containers:
        take_number.append(c)
        total += c
        if total > target:
            return take_number
        
def init_check(lst, target):
    """
    Calculate the min and max qty of numbers needed to reach the target value. 
    """
    lst.sort()
    temp_lst = get_target_value(lst, target)
    #print(temp_lst)
    #print(f'target is {target}. if we take the number from min, we need at least {len(temp_lst)} numbers')
    a = len(temp_lst)
    lst.reverse()
    temp_lst = get_target_value(lst, target)
    #print(temp_lst)
    #print(f'target is {target}. if we take the number from max, we need at least {len(temp_lst)} numbers')
    b = len(temp_lst)
    return b, a

def senerio(qty, lst):
    output_lst = []
    for i, c in enumerate(lst):
        _lst_sub = lst[i+1:].copy()
        if qty > 2:
            o_lst = senerio(qty-1, _lst_sub)
        elif qty ==2:
            o_lst = item2lst(_lst_sub)
        _sub_output_lst = add_item2lst(c, o_lst)
        
        output_lst.extend(_sub_output_lst)
    return output_lst  

def item2lst(lst):
    """Create a list of list. [1,2,3] output [[1], [2], [3]]"""
    _empty_lst = []
    final_lst = []
    for item in lst:
        _e_lst = _empty_lst.copy()
        _e_lst.append(item)
        final_lst.append(_e_lst)
    return final_lst   

def add_item2lst(i, lst_of_lst):
    """
    add one item to lst of lst, add_item2lst(1, [[2],[3],[4]]) output [[2, 1], [3, 1], [4, 1]]
    """
    output_l = []
    for item in lst_of_lst:
        item.append(i)
        output_l.append(item)
    return output_l

# Read the input from the file and close it
with open('./input/2015/q17.txt') as f:
    containers = []
    for c in f.readlines():
        containers.append(int(c))
f.close()

# Get the min and max qty of number needed to reach the 150. 
min_qty, max_qty = init_check(containers, 150)

############### Part 1  ###################
result_lst = []
for i in range(min_qty, max_qty):
    for lst in senerio(i, containers):
        if sum(lst) == 150:
            result_lst.append(lst)
print(f"Part 1: There are total {len(result_lst)} ways to store 150.")
del i, lst

############## Part 2  ####################
min_result = []
for i in range(min_qty, max_qty):
    while not min_result:
        for lst in senerio(i, containers):
            if sum(lst) == 150:
                min_result.append(lst)
print(f"Part 2: Inside of those ways, {len(min_result)} ways to store 150 and only use {len(min_result[0])} containers.")   