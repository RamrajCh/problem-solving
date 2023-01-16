def main(L, target):
    hash = []
    for l in L:
        if target - l in hash:
            return (target - l, l)
        hash.append(l)

if __name__ == "__main__":
    # Input: [1, 2, 3, 4, 5], 5
    # standard_input = "[1,2,3,4,5],5"
    S = input()
    L, target = S.split("],")
    L = list(map(lambda x:int(x), L[1:].split(",")))
    two_sum_solution = main(L, int(target))
    
    print(f"Input: {S}")
    if two_sum_solution:
        print(f"Output: {two_sum_solution}")
    else:
        print("No solution")