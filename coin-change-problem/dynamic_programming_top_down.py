def coin_change(coins, target):
    memo = [target+1 for i in range(target+1)]
    memo[0] = 0
    
    for i in range(1, target+1):
        for coin in coins:
            if coin <= i:
                memo[i] = min(memo[i], memo[i-coin]+1)
    
    print(memo[target])

if __name__ == "__main__":
    changes = [2,5,9,10]
    target = 30
    coin_change(changes, target)