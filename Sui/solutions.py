import numpy as np

def day10_2015 (textInput, n):
    input = textInput
    inputArray = np.array (list(map(int, input)))
    for i in range(n):
        inputArray = look_and_say(inputArray)
    return len(inputArray)

def look_and_say (inputArray):
    arrayNext1 = np.append (np.delete (inputArray, 0), 0)
    arrayNext2 = np.append (np.delete (inputArray, (0, 1)), (0, 0))
    bArrays = np.vstack (((inputArray == arrayNext1), (inputArray == arrayNext2))).T
    nums = np.apply_along_axis (find_repeatance, 1, bArrays)
    mask = 1 == np.append(1, np.delete(nums, -1))
    output = (np.vstack ((nums[mask],inputArray[mask])).T).ravel()
    return output

def find_repeatance (bArray):
    try:
        n = 1 + np.where (bArray == False)[0][0]
    except:
        n = 3
    return n

print (day10_2015("1113222113",50))
