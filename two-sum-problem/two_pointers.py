def main(L, sum):
    start = 0
    end = len(L) - 1
    
    while True:
        if start == end:
            break
        if L[start] + L[end] == sum:
            return (L[start], L[end])
        elif L[start] + L[end] < sum:
            start += 1
        else:
            end -= 1
    return None
    
    ...

if __name__ == "__main__":
    # Input: [1, 2, 3, 4, 5], 5
    # standard_input = "[2,1,3,6,4,5],5"
    S = input()
    L, sum = S.split("],")
    L = list(map(lambda x:int(x), L[1:].split(",")))
    # sort the list
    L.sort()
    
    two_sum_solution = main(L, int(sum))
    
    print(f"Input: {S}")
    if two_sum_solution:
        print(f"Output: {two_sum_solution}")
    else:
        print("No solution")