import pandas as pd
import numpy as np


str_input = """Sprinkles: capacity 5, durability -1, flavor 0, texture 0, calories 5
PeanutButter: capacity -1, durability 3, flavor 0, texture 0, calories 1
Frosting: capacity 0, durability -1, flavor 4, texture 0, calories 6
Sugar: capacity -1, durability 0, flavor 0, texture 2, calories 8
"""

# Use input data to generate dataframe and array
info = []
arr = []
for line in str_input.split('\n')[:-1]:
    # sl is splited line
    sl = line.split()
    info.append([sl[0][:-1], int(sl[2][:-1]), int(sl[4][:-1]), int(sl[6][:-1]), int(sl[8][:-1]), int(sl[-1])])

headers = ['name', 'capacity', 'durability', 'flavor', 'texture', 'calories']

df = pd.DataFrame(data = info, columns = headers)
arr = df[['capacity', 'durability', 'flavor', 'texture', 'calories']].to_numpy()

# Generate two numbers, the sum of them are equal to 'num'
def recipe(num):
    recipe_lst = []
    for i in range(num + 1):
        recipe_lst.append([i, num - i])
    return recipe_lst

# Generate 4 numbers, the sum of them are equal to 'num'
def f_element_recipe(num):
    recipe_lst = []
    for line in recipe(num):
        part1 = recipe(line[0])
        part2 = recipe(line[1])
        for p1 in part1:
            for p2 in part2:
                recipe_lst.append([p1[0], p1[1], p2[0], p2[1]])
    return recipe_lst

# replace negative numbers in list by zero, output new number list.
def check_negtive_num(num_lst):
    new_lst = []
    for n in num_lst:
        if n < 0:
            new_lst.append(0)
        else:
            new_lst.append(n)
    return new_lst

############### Executation ################
if __name__ == "__main__":
    one_hundred_spoon = f_element_recipe(100)

    recipe_result_p1 = []
    for r in one_hundred_spoon:
        score = np.prod(check_negtive_num(np.dot(r, arr))[:-1])
        recipe_result_p1.append(score)
    max_p1 = max(recipe_result_p1)

    recipe_result_p2 = []
    for r in f_element_recipe(100):
        recipe_dot_result = np.dot(r, arr)
        if recipe_dot_result[-1] == 500:
            recipe_result_p2.append(np.prod(check_negtive_num(recipe_dot_result[:-1])))
    max_p2 = max(recipe_result_p2)
    
    i, j, m, n = one_hundred_spoon[recipe_result_p1.index(max_p1)]
    print(df)
    print(f"The best P1 recipe: {i} teaspoons of Sprinkles, {j} teaspoons of PeanutButter, {m} teaspoons of Frosting and {n} teaspoons of Sugar.")
    print(f"The score of this recipe is {max_p1} ")

    i, j, m, n = one_hundred_spoon[recipe_result_p1.index(max_p2)]
    print(f"The best P2 recipe: {i} teaspoons of Sprinkles, {j} teaspoons of PeanutButter, {m} teaspoons of Frosting and {n} teaspoons of Sugar.")
    print(f"The score of this recipe is {max_p2} ")