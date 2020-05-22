import sys
sys.path.append("..")
import re
from mytools import tools
START_LIST = tools.read_file("line")
START_MOLECULE = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

def one(reactions, molecule):
    print("starting 1")
    results = set()
    for i, v in enumerate(reactions):
        reaction = v.split(" => ")
        mol_list = molecule.split(reaction[0])
        if len(mol_list) > 1:
            for j, k in enumerate(mol_list):
                if j < len(mol_list)-1:
                    a = reaction[0].join(mol_list[:j+1])
                    b = reaction[0].join(mol_list[j+1:])
                    new = [a, reaction[1], b]
                    results.add("".join(new))
        else:
            continue
    print(len(results))
    return(results)

one(START_LIST, START_MOLECULE)

def two(reactions, molecule):
    '''
    General rule
    Notice there are some element that does not iterate further with reaction
    So every time this element show 1 time, the reaction run 1 time
    '''
    # find all the elemnt and the length of all the final modecule
    el_all = re.findall(r"[A-Z][a-z]*", molecule)
    el_all_set = set(el_all)
    print(el_all)
    print(len(el_all))

    # find el that can do further reactions
    reaction_variables = set(map(lambda el: el.split(" ")[0], reactions))
    print(reaction_variables)

    # find el that cannot do further reactions
    el_no_reaction = el_all_set - reaction_variables
    print(el_no_reaction)

    # put these element in a list and find their appearance time in the molecule
    counter = {el:el_all.count(el) for el in el_no_reaction}
    print(counter)  # the result is {'Rn': 31, 'C': 1, 'Ar': 31, 'Y': 8}

    # now, eye ball analysis
    # for the 4 types Rn, C, Ar, Y, everytime there is Rn and Ar come, with C and Y
    # so must be Rn times reaction happen to get here
    no_reaction_el_step_count = counter["Rn"]
    print(no_reaction_el_step_count)

    # with this Rn type of reaction, no reaction element(the 4 elements) should add this much length to the final module
    no_reaction_el_increase = sum(counter.values())
    print(no_reaction_el_increase)

    # addtionally, every time Rn is there, the variable element + 1
    # every time Y is there, the varialbe element + 1
    # every time C is there, the varialbe does not change quantity, and reduce once the Rn adding
    # so the overall variable add by reaction wiht no_reaction elemenet is this
    no_reaction_el_increase_variable = counter["Rn"]+counter["Y"]-counter["C"]
    
    # the variable_self_add is added by normal reaction, where 1 change to 2, so every reaction element increase 1 in the molecule
    variable_self_add = len(el_all) - no_reaction_el_increase - no_reaction_el_increase_variable
    print(variable_self_add)

    # the reaction time happend within reactive variables self iteration
    variable_self_add_time = variable_self_add -1 

    # final count how many times reaction happened
    result = variable_self_add_time + no_reaction_el_step_count
    print(variable_self_add_time + no_reaction_el_step_count)
    return result

two(START_LIST, START_MOLECULE)