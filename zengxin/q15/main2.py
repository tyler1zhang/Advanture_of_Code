import main1 as base
start_list = base.start_list

def cal_score_with_calories(parameters: list, recipe: list):
    total_score = 0
    # get the property to iterate first, for exmaple capcity as the first i, leave the calories
    properties = len(parameters[0]) - 1
    total_score = 1
    for i in range(properties):
        property_score = 0
        calories_score = 0
        for j in range(len(recipe)):
            property_score += parameters[j][i] * recipe[j]
            calories_score += parameters[j][len(parameters[0]) - 1] * recipe[j]
        if property_score < 0:
            property_score = 0
        elif calories_score != 500:
            property_score = 0
        total_score *= property_score
    return total_score

def cal_recipi_combination_score(parameters):
    # the ingredients type is 4, so the recipe here is 4, so to for loop 4 times
    for i in range(101):
        for j in range(101-i):
            for k in range(101-i-j):
                for l in range(101-i-j-k):
                    recipe = [i, j, k, l]
                    recipe_score = cal_score_with_calories(parameters, recipe)
                    yield recipe_score
def main(input):
    parameters = base.get_parameter_list(input)
    final_score = cal_recipi_combination_score(parameters)
    # print(list(final_score))
    highest_score = max(final_score)
    print(highest_score)

main(start_list)