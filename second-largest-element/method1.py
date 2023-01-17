def second_largest(S):
    max_ = S[0]
    second_max = S[0]
    
    for i in range(1, len(S)):
        if S[i] > max_:
            second_max = max_
            max_ = S[i]
            
        elif S[i] > second_max:
            second_max = S[i]
    
    print(second_max)

if __name__ == "__main__":
    # standard_input = "1,2,4,3,7,9,10,50,3,99,4,35,2,5,3,7,23,56,34,65,90"
    # standard_input = "1,2,3,4,5,10"
    S = input()
    # S = "1,2,3,4,5,10"
    S = list(map(lambda x:int(x), S.split(",")))
    second_largest(S)