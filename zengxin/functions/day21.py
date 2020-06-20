import collections
import itertools
# define play equip situations
# define winning situation on each equip situations, if win, record the cost
def day21():
    # define boss and player
    Profile = collections.namedtuple("Profile", ["HP", "Damage", "Armor"])
    boss = Profile(104, 8, 1)
    player_damage, player_armor  = 0, 0

    # define items to choose
    Items = collections.namedtuple("Items", "Cost, Damage, Armor")
    Weapons = list(map(Items._make, [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]))
    # add no choose condition as [0, 0, 0]
    Armors = list(map(Items._make, [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5], [0, 0, 0]])) 
    Rings = list(map(Items._make, [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3], [0, 0, 0]]))

    total_cost_win = []
    total_cost_lose = []
    # player equip situations evaluation to if win
    for w, a, r1, r2 in itertools.product(Weapons, Armors, Rings, Rings):
        if r1.Cost != r2.Cost or r1.Cost == 0 or r2.Cost == 0:
            player_damage = w.Damage+a.Damage+r1.Damage+r2.Damage
            player_armor = w.Armor+a.Armor+r1.Armor+r2.Armor
            # evaluate winning situation, considering player attack first
            boss_drop = max(1,player_damage-boss.Armor)
            player_drop = max(1, boss.Damage-player_armor)
            # win conditions
            if boss_drop > player_drop:
                total_cost_win.append(w.Cost+a.Cost+r1.Cost+r2.Cost) 
            # as player attack first
            elif boss_drop == player_drop and 100%boss_drop != 0 and boss_drop-(100%boss_drop)>=4:
                total_cost_win.append(w.Cost+a.Cost+r1.Cost+r2.Cost) 
            else: 
                total_cost_lose.append(w.Cost+a.Cost+r1.Cost+r2.Cost)
    return min(total_cost_win), max(total_cost_lose)

def day21part1():
    return day21()[0]
    
def day21part2():
    return day21()[1]

print(day21part1())
print(day21part2())



