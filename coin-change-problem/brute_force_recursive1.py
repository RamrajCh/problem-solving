def coin_change(coins, target, result, current_combination=[]):
    if target == 0:
        result.append(current_combination.copy())
    
    else:
        for coin in coins:
            if coin <= target:
                current_combination.append(coin)
                coin_change(coins, target-coin, result, current_combination=current_combination)
                current_combination.pop()
        

if __name__ == "__main__":
    changes = [1,2,10]
    target = 17
    result = []
    coin_change(changes, target, result)
    print(result[-1])