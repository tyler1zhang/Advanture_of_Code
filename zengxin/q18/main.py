import sys
sys.path.append("..")

from mytools import tools
START_LIST = tools.read_file("line")

def data_transform(data_input):
    a = list(map(lambda el: list(map(lambda el: 1 if el == "#" else 0, el)), data_input))
    all_zero = [0 for i in range(100)]
    b = [all_zero, *a, all_zero]
    c = list(map(lambda el: [0, *el, 0], b))
    return c

def cal_one_round(data):
    result = [a[:] for a in data]
    # need to break 2 layers
    # need to break the result to the elemental layer, otherwise the calculation cannot work
    # is only break one layer like result = data[:], then list of result[0] and data[0] is pointing to the same list
    # can use the id to check this, so every time data[i][j] change, result[i][j] also change

    # can uncomment the following 3 lines to check this one, check the id
    # result = data[:]
    # print(id(result[0]))
    # print(id(data[0]))

    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            if data[i][j] == 1 and check_neighbour(data, i, j, "on"):
                # print(data[i][j])
                # print(result[i][j])
                result[i][j] = 0 
                # print(data[i][j])
                # print(result[i][j])
            elif data[i][j] == 0 and check_neighbour(data, i, j, "off"):
                result[i][j] = 1
    return result

def check_neighbour(data, i, j, condition):
    sum_all = 0
    for a in range(i-1, i+2):
        for b in range(j-1, j+2):
            sum_all += data[a][b]
    if (condition == "on" and sum_all not in (3, 4)) or (condition == "off" and (sum_all == 3)):
        return True
    return False

def one(data_input):
    ready_data = data_transform(data_input)
    for i in range(100):
        ready_data = cal_one_round(ready_data)
    result = sum(map(sum, ready_data))
    print("one is ", result)
    return result

one(START_LIST)

###########################################################################
######################   Part 2     #######################################

def cal_one_round_two(data):
    result = [a[:] for a in data]
    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            if data[i][j] == 1 and check_neighbour(data, i, j, "on"):
                if (i,j) not in [(1,1), (1,100), (100,1), (100,100)]:
                    result[i][j] = 0 
            elif data[i][j] == 0 and check_neighbour(data, i, j, "off"):
                result[i][j] = 1
    return result

def two(data_input):
    ready_data = data_transform(data_input)
    ready_data[1][1]=ready_data[1][100]=ready_data[100][1]=ready_data[100][100]=1
    for i in range(100):
        ready_data = cal_one_round_two(ready_data)
    result = sum(map(sum, ready_data))
    print("two is ", result)
    return result


two(START_LIST)