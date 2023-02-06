def fibonacci(N):
    fib = [0 for _ in range(N+1)]
    fib[1] = 1
    for n in range(2, N+1):
        fib[n] = fib[n-1] + fib[n-2]
    return fib[N]

if __name__ == "__main__":
    N = 10
    print(fibonacci(N))