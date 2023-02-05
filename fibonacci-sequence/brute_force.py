def main(N):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(1,N-1):
        c = a + b
        print(c)
        a = b
        b = c

if __name__ == "__main__":
    N = 10
    main(N)