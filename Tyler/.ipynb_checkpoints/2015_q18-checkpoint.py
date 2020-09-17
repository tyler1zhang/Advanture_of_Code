import numpy as np
from itertools import islice


d18_input_file_path = './input/2015/q18.txt'
with open(d18_input_file_path) as f:
    grid_char = []
    for line in f.readlines():
        grid_char.append(list(line))
        
#convert str to int type, data structure is np.array        
grid = np.zeros((100, 100), dtype = 'int')
for i in range(100):
    for j in range(100):
        if grid_char[i][j] == '#':
            grid[i][j] = 1
            
def x_shift(distance, arr):
    """
    shift the arr along axis = 1 by distance 
    
    Arguments:
    distance -- int, if distance >0, toward right side.
    arr -- current array, dtype = int
    
    Returns:
    new_arr -- after shift
    """
    c_zeros = np.zeros((arr.shape[0], 1), dtype = 'int')
    if distance < 0:
        new_arr = np.concatenate((arr[:, -distance:], c_zeros), axis = 1)
    elif distance >0:
        new_arr = np.concatenate((c_zeros, arr[:, :-distance]), axis = 1)
    else:
        new_arr = arr
    
    return new_arr

def y_shift(distance, arr):
    """
    shift the arr along axis = 0 by distance 
    
    Arguments:
    distance -- int, if distance >0, toward upper side.
    arr -- current array, dtype = int
    
    Returns:
    new_arr -- after shift
    """
    r_zeros = np.zeros((1, arr.shape[0]), dtype = 'int')
    if distance < 0:
        new_arr = np.concatenate((r_zeros, arr[:distance, :]), axis = 0)
    elif distance > 0:
        new_arr = np.concatenate((arr[distance:, :], r_zeros), axis = 0)
    else:
        new_arr = arr
    
    return new_arr

def neighbor(x, y, arr):
    """
    the function to return a new arr that shifted current arr to direction.
    
    Arguments:
    direction -- tuple like (1, 1) means shift to the right-up
    arr       -- current array input
    
    Returns:
    array after shift
    """ 
    
    if x == 0 and y == 0:
        return np.zeros(arr.shape, dtype = 'int')
    else:
        x_shifted_arr = x_shift(x, arr)
        return y_shift(y, x_shifted_arr)
    
def neighbor_counts(arr):
    """
    function to count how many light were on at this coordinate of arr.
    """
    N = np.zeros(arr.shape, dtype = 'int')
    d = [-1, 0, 1]
    for i in d:
        for j in d:
            N += neighbor(i, j, arr)
    return N

def next_display(arr):
    """
    return the next display of arr, based on the rule.
    """
    next_arr = np.zeros(arr.shape, dtype = 'int')
    neighbor_counts_arr = neighbor_counts(arr)
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i, j] == 1:
                if neighbor_counts_arr[i, j] in [2, 3]:
                    next_arr[i, j] = 1
            else:
                if neighbor_counts_arr[i, j] == 3:
                    next_arr[i, j] = 1
    return next_arr

def show_display(arr):
    """
    generator to get next display array
    """
    base_arr = arr
    while True:
        base_arr = next_display(base_arr)
        yield base_arr

def corner_on(arr):
    new_arr = arr
    new_arr[0,0] = 1
    new_arr[0, arr.shape[1]-1] = 1
    new_arr[arr.shape[0]-1, 0] = 1
    new_arr[arr.shape[0]-1, arr.shape[1]-1] = 1
    return new_arr

def part2(arr):
    base_arr = corner_on(arr)
    m = 99
    while True:
        base_arr = corner_on(next_display(base_arr))
        yield base_arr
        
n = 100
part1_arr = list(islice(show_display(grid), n-1, n))[0]
print(f"After {n} times flash, there are {np.sum(part1_arr)} lights on for part1.")
print()
part2_arr = list(islice(part2(grid), n-1, n))[0]
print(f"After {n} times flash, there are {np.sum(part2_arr)} lights on for part2.")