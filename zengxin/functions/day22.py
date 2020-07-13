'''
    Magic Missile costs 53 mana. It instantly does 4 damage.
    Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
    Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
    Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
    Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

    missile 13 mana per damage, drain 36 mana per damage, heal 2 hp, shield add 7 armor, poison 10 mana per damage, recharge earn 505-229=276 mana

    So
    Always use poison, it is cheapest damage and last longer
    Use the recharge to make sure it does not dry out the mana 
    Put on shield to reduce the damage of the boss from 9 to 2, in this combination, the boss always loss more than the player, keeping this till palyer win
    logic is : check if can strike boss, put poison priority to shield, as we need fast win
'''

def day22part1():

    class Boss:
        def __init__(self, hp, damage, poison_timer):
            self.hp = hp
            self.damage = damage
            self.poison_timer = poison_timer
    boss = Boss(51, 9, 0)
    
    class Player: 
        def __init__(self, hp, mana, armor, shield_timer, recharge_timer):
            self.hp = hp
            self.mana = mana
            self.armor = armor
            self.shield_timer = shield_timer
            self.recharge_timer = recharge_timer
    player = Player(50, 500, 0, 0, 0)
    
    class Drug:
        def __init__(self, missile, drain, shield, poison, recharge):
            self.missile = missile
            self.drain = drain
            self.shield = shield
            self.poison = poison
            self.recharge = recharge
    cost_of_drugs = Drug(53, 73, 113, 173, 229)
    drugs_on_shelf = Drug(1, 1, 1, 1, 1)

    mana_usage = []
    
    # to clear the starting turn states
    def start_turn():
        if boss.poison_timer > 1:
            boss.hp -= 3
            boss.poison_timer -= 1
        elif boss.poison_timer == 1:
            boss.hp -= 3
            boss.poison_timer -= 1
            drugs_on_shelf.poison = 1

        if player.shield_timer > 1:
            player.armor = 7
            player.shield_timer -= 1
        elif player.shield_timer == 1:
            player.shield_timer -= 1
            drugs_on_shelf.shield = 1
            player.armor = 0

        if player.recharge_timer > 1:
            player.mana += 101
            player.recharge_timer -= 1
        elif player.recharge_timer == 1:
            player.mana += 101
            player.recharge_timer -= 1
            drugs_on_shelf.recharge = 1

    def evaluate_win():
        if boss.hp <= 0:
            print("player win") 
            return mana_usage
        elif player.mana < 0 or player.hp <= 0:
            print("boss win")
            return mana_usage
    
    def use_missile():
        player.mana -= cost_of_drugs.missile
        mana_usage.append(cost_of_drugs.missile)
        boss.hp -= 4
    
    def use_drain():
        boss.hp -= 2
        player.hp += 2
        player.mana -= cost_of_drugs.drain
        mana_usage.append(cost_of_drugs.drain)
    
    def use_recharge():
        player.mana -= cost_of_drugs.recharge
        mana_usage.append(cost_of_drugs.recharge)
        player.recharge_timer = 5
        drugs_on_shelf.recharge = 0

    def use_poison():
        player.mana -= cost_of_drugs.poison
        mana_usage.append(cost_of_drugs.poison)
        boss.poison_timer = 6
        drugs_on_shelf.poison = 0

    def use_shield():
        player.mana -= cost_of_drugs.shield
        mana_usage.append(cost_of_drugs.shield)
        player.shield_timer = 6     
        drugs_on_shelf.shield = 0

    def player_make_choice():
        # calcuate when to use missile to finish the boss
        # 2 * player.shield_timer / 2 + 9 * (player_turn_to_death-player.shield_timer) / 2 < player.hp
        # boss.poison_timer * 3 + boss_turn_to_death_fastest // 2 * 4 > boss.hp
        player_turn_to_death = (player.hp + 3.5 * player.shield_timer) // 4.5 + 1 
        boss_turn_to_death_fastest = (boss.hp - boss.poison_timer * 3) // 2 

        if boss_turn_to_death_fastest < player_turn_to_death and player.mana >= player_turn_to_death * cost_of_drugs.missile // 2 :
            use_missile()
            print("attack to the end")
        # use drain to make a difference on the turn to death
        elif boss_turn_to_death_fastest == player_turn_to_death and player.mana >= player_turn_to_death * cost_of_drugs.missile // 2 :
            use_drain()
        elif drugs_on_shelf.recharge == 1 and player.mana >= cost_of_drugs.recharge and player.mana <= cost_of_drugs.recharge + cost_of_drugs.poison:
            use_recharge()
        elif drugs_on_shelf.poison == 1 and player.mana >= cost_of_drugs.shield:
            use_poison()
        elif drugs_on_shelf.shield == 1 and player.mana >= cost_of_drugs.shield:
            use_shield()
        else:
            use_drain()
    
    def boss_attack():
        attack_force = boss.damage - player.armor
        player.hp -= max(1, attack_force)

    # max 500 turn surely finished
    for i in range(500):
        start_turn()
        if evaluate_win():
            print("end with round ", i)
            print(mana_usage)
            result = evaluate_win()
            return sum(result)
        player_make_choice()
        start_turn()
        if evaluate_win():
            print("end with rount ", i)
            print(mana_usage)
            result = evaluate_win()
            return sum(result)
        boss_attack()
        if evaluate_win():
            print("end with rount ", i)
            print(mana_usage)
            result = evaluate_win()
            return sum(result)
        print(boss.hp, player.hp, player.mana)
        print("")


print(day22part1())

def day22part2():

    class Boss:
        def __init__(self, hp, damage, poison_timer):
            self.hp = hp
            self.damage = damage
            self.poison_timer = poison_timer
    boss = Boss(51, 9, 0)
    
    class Player: 
        def __init__(self, hp, mana, armor, shield_timer, recharge_timer):
            self.hp = hp
            self.mana = mana
            self.armor = armor
            self.shield_timer = shield_timer
            self.recharge_timer = recharge_timer
    player = Player(50, 500, 0, 0, 0)
    
    class Drug:
        def __init__(self, missile, drain, shield, poison, recharge):
            self.missile = missile
            self.drain = drain
            self.shield = shield
            self.poison = poison
            self.recharge = recharge
    cost_of_drugs = Drug(53, 73, 113, 173, 229)
    drugs_on_shelf = Drug(1, 1, 1, 1, 1)

    mana_usage = []
    
    # to clear the starting turn states
    def start_turn():
        if boss.poison_timer > 1:
            boss.hp -= 3
            boss.poison_timer -= 1
        elif boss.poison_timer == 1:
            boss.hp -= 3
            boss.poison_timer -= 1
            drugs_on_shelf.poison = 1

        if player.shield_timer > 1:
            player.armor = 7
            player.shield_timer -= 1
        elif player.shield_timer == 1:
            player.shield_timer -= 1
            drugs_on_shelf.shield = 1
            player.armor = 0

        if player.recharge_timer > 1:
            player.mana += 101
            player.recharge_timer -= 1
        elif player.recharge_timer == 1:
            player.mana += 101
            player.recharge_timer -= 1
            drugs_on_shelf.recharge = 1

    def evaluate_win():
        if boss.hp <= 0:
            print("player win") 
            return mana_usage
        elif player.mana < 0 or player.hp <= 0:
            print("boss win")
            return mana_usage
    
    def use_missile():
        player.mana -= cost_of_drugs.missile
        mana_usage.append(cost_of_drugs.missile)
        boss.hp -= 4
    
    def use_drain():
        boss.hp -= 2
        player.hp += 2
        player.mana -= cost_of_drugs.drain
        mana_usage.append(cost_of_drugs.drain)
    
    def use_recharge():
        player.mana -= cost_of_drugs.recharge
        mana_usage.append(cost_of_drugs.recharge)
        player.recharge_timer = 5
        drugs_on_shelf.recharge = 0

    def use_poison():
        player.mana -= cost_of_drugs.poison
        mana_usage.append(cost_of_drugs.poison)
        boss.poison_timer = 6
        drugs_on_shelf.poison = 0

    def use_shield():
        player.mana -= cost_of_drugs.shield
        mana_usage.append(cost_of_drugs.shield)
        player.shield_timer = 6     
        drugs_on_shelf.shield = 0

    def player_make_choice():
        # calcuate when to use missile to finish the boss
        # 2 * player.shield_timer / 2 + 9 * (player_turn_to_death-player.shield_timer) / 2 + player_turn_to_death /2 < player.hp
        # boss.poison_timer * 3 + boss_turn_to_death_fastest // 2 * 4 > boss.hp
        player_turn_to_death = (player.hp + 3.5 * player.shield_timer) // 5 + 1
        boss_turn_to_death_fastest = (boss.hp - boss.poison_timer * 3) // 2 

        if boss_turn_to_death_fastest < player_turn_to_death and player.mana >= player_turn_to_death * cost_of_drugs.missile // 2 :
            use_missile()
            print("attack to the end")
        # use drain to make a difference on the turn to death
        elif boss_turn_to_death_fastest == player_turn_to_death and player.mana >= player_turn_to_death * cost_of_drugs.missile // 2 :
            use_drain()
        elif drugs_on_shelf.recharge == 1 and player.mana >= cost_of_drugs.recharge and player.mana <= cost_of_drugs.recharge + cost_of_drugs.poison:
            use_recharge()
        elif drugs_on_shelf.poison == 1 and player.mana >= cost_of_drugs.shield:
            use_poison()
        elif drugs_on_shelf.shield == 1 and player.mana >= cost_of_drugs.shield:
            use_shield()
        else:
            use_drain()
    
    def boss_attack():
        attack_force = boss.damage - player.armor
        player.hp -= max(1, attack_force)

    # max 500 turn surely finished
    for i in range(500):
        player.hp -= 1
        if evaluate_win():
            print("end with round ", i)
            print(mana_usage)
            result = evaluate_win()
            return sum(result)
        start_turn()
        if evaluate_win():
            print("end with round ", i)
            print(mana_usage)
            result = evaluate_win()
            return sum(result)
        player_make_choice()
        start_turn()
        boss_attack()
        if evaluate_win():
            print("end with rount ", i)
            print(mana_usage)
            result = evaluate_win()
            return sum(result)
        print("player hp", player.hp)
        print("player mana", player.mana)
        print("boss hp", boss.hp)
        print("")

print(day22part2())