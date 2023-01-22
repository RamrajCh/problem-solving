def coin_change(coins, target):
    soln = []
    while sum(soln) != target:
        current_sum = sum(soln)
        if max(coins) <= (target - current_sum):
            soln.append(max(coins))
        else:
            coins.remove(max(coins))
    print(soln)
            

if __name__ == "__main__":
    changes = [1,2,10,20,40]
    target = 37
    coin_change(changes, target)