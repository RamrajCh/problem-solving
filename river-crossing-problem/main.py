def check_contsraints(state):
    #  check if wolf and goat are alone
    # if (
    #     (not state[0] and not state[2]) or
    #     (state[1] and state[3]) or
    #     (state[0] and state[2]) or
    #     (state[0] and not state[1] and state[3]) or
    #     (not state[1] and state[2] and not state[3])
    # ): return True
    if (
        (not state[0] and not state[2]) or
        (state [0] and state[1] and state[3]) or
        (state[0] and state[2]) or
        (not state[1] and state[2] and not state[3])
    ): return True
    
    return False

def move_farmer(state):
    return [int(not state[0]), state[1], state[2], state[3]]

def move_wolf(state):
    if state[0] == state[1]:
        return [int(not state[0]), int(not state[1]), state[2], state[3]]

def move_goat(state):
    if state[0] == state[2]:
        return [int(not state[0]), state[1], int(not state[2]), state[3]]

def move_cabbage(state):
    if state[0] == state[3]:
        return [int(not state[0]), state[1], state[2], int(not state[3])]

def main():
    states = [[0,0,0,0]]
    goal_path = []
    while states[0] != [1,1,1,1]:
        current = states.pop(0)

        goal_path.append(current)
        # move farmer only
        F = move_farmer(current)
        if F and check_contsraints(F) and F not in goal_path:
            move = "left bank to right bank" if F[0] == 1 else "right bank to left bank"
            print(f"Farmer is moved from {move}\t\t {current} -> {F}")
            states.append(F)
            continue
        
        # move wolf
        W = move_wolf(current)
        if W and check_contsraints(W) and W not in goal_path:
            move = "left bank to right bank" if W[1] == 1 else "right bank to left bank"
            print(f"Farmer and wolf are moved from {move}\t\t {current} -> {W}")
            states.append(W)
            continue
        
        # move goat
        G = move_goat(current)
        if G and check_contsraints(G) and G not in goal_path:
            move = "left bank to right bank" if G[2] == 1 else "right bank to left bank"
            print(f"Farmer and goat are moved from {move}\t\t {current} -> {G}")
            states.append(G)
            continue
        
        # move cabbage
        C = move_cabbage(current)
        if C and check_contsraints(C) and C not in goal_path:
            move = "left bank to right bank" if C[3] == 1 else "right bank to left bank"
            print(f"Farmer and cabbage are moved from {move}\t\t {current} -> {C}")
            states.append(C)
            continue
    
    print("All things have successfully crossed the river.")
    
if __name__ == "__main__":
    main()