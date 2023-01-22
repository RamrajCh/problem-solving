def coin_change(coins, target):
    combinations = []
    stack = [(0,[])]
    
    while stack:
        total, combination = stack.pop()
        if total == target:
            combinations.append(combination)
        
        for coin in coins:
            if total + coin <= target:
                stack.append((total+coin, combination+[coin]))
    
    soln = (float('inf'), [])
    
    for com in combinations:
        change = sum(com)
        if target == change:
            L = len(com)
            if L < soln[0]:
                soln = (L, com)
    print(soln[1]) if soln[1] else print("No solution")
        

if __name__ == "__main__":
    changes = [1,2,10]
    target = 17
    coin_change(changes, target)