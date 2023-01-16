def main(L, sum):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] + L[j] == sum:
                return (L[i], L[j])
    return None

if __name__ == "__main__":
    # Input: [1, 2, 3, 4, 5], 5
    # standard_input = "[1,2,3,4,5],5"
    S = input()
    L, sum = S.split("],")
    L = list(map(lambda x:int(x), L[1:].split(",")))
    two_sum_solution = main(L, int(sum))
    
    print(f"Input: {S}")
    if two_sum_solution:
        print(f"Output: {two_sum_solution}")
    else:
        print("No solution")
