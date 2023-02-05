def fibonacci(N):
    a = 0
    b = 1
    for i in range(2,N+1):
        c = a + b
        a = b
        b = c
    return(c)

if __name__ == "__main__":
    N = 10
    print(fibonacci(N))