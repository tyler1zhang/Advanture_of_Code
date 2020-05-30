if __name__ == "__main__":

    f = open('./input/2015/q1.txt', "r")

    up_down = 0
    i = 0
    while 1:
        char = f.read(1)
        if not char: break
        elif char == "(":
            up_down += 1
        elif char == ")":
            up_down -= 1
        
        i += 1
        if up_down == -1:
            print(f"Part 2 result is {i}")
            break

    f.close()        