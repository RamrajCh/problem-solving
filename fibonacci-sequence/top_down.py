def fibonacci(N, memo):
    if memo[N]:
        return memo[N]
    elif N <=1:
        result = N
    else:
        result = fibonacci(N-1, memo) + fibonacci(N-2, memo)
    memo[N] = result    
    return result
    

if __name__ == "__main__":
    N = 10
    memo = [None for _ in range(N+1)]
    print(fibonacci(N, memo))