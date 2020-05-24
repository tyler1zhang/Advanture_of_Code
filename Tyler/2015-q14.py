#import 

racing_time = 2503

def individual_distance(name, lst, race_time):
    # Calculate one Reindeer flying distance after race_time. 
    speed = lst[0]
    duration = lst[1]
    rest_time = lst[2]
    cycles = race_time // (duration + rest_time)
    remainder = race_time % (duration + rest_time)
    if remainder >= duration:
        distance = speed * duration * (cycles + 1)
    else:
        distance = speed * duration * cycles + speed * remainder
    
    return distance

def find_names_by_value(v, dic):
    # Based on the value, find all names(key) with same value. Return one name list
    dic_copy = dic.copy()
    names = []
    while True:
        try:
            name = list(dic_copy.keys())[list(dic_copy.values()).index(v)]
            del dic_copy[name]
            names.append(name)
        except:
            break
    
    return names

def find_winner(info_dic, t):
    # Calculate all Reindeers results. 
    racing_result = {}
    for reindeer in info_dic:
        d = individual_distance(reindeer, info_dic[reindeer], t)
        racing_result[reindeer] = d

    longest_dis = max(racing_result.values())
    winner = find_names_by_value(longest_dis, racing_result)
    return winner, longest_dis

if __name__ == "__main__":
    # Input data from file
    with open("2015-Q14_tyler.txt") as f:
        althelites = {}
        names = []
        for line in f.readlines():
            info = line.split()
            althelites[info[0]] = [int(info[3]), int(info[6]), int(info[-2])]
            names.append(info[0])
    f.close() 

    w, l = find_winner(althelites, racing_time)
    print(f"Part 1: The winner is {w}. His or her result is {l}")

    # Initialize the score_board, every Reindeer has 0 score.  
    score_board = {}
    for n in names:
        score_board[n] = 0

    for t in range(1, 2504):
        # winners at specific time is w_s, the longest_d is l_d
        w_s, l_d = find_winner(althelites, t)
        for n in w_s:
            score_board[n] += 1
    
    highest_score = max(score_board.values())
    score_winners = find_names_by_value(highest_score, score_board)
    print(f"Part 2: The winner is {score_winners} and his or her score is {highest_score}")



