def second_largest(S):
    # Sort S in descending order
    
    # Sorting as bubble sort
    n = len(S)
    
    for i in range(n):
        for j in range(n-i-1):
            if S[j+1] >= S[j]:
                temp = S[j]
                S[j] = S[j+1]
                S[j+1] = temp
    
    # Get second element
    
    print(S[1])
    

if __name__ == "__main__":
    # standard_input = "91,20,4,3,7,9,100,50,3,99,4,35,2,5,3,7,23,56,34,65,90"
    # standard_input = "1,2,3,4,5,10"
    S = input()
    # S = "1,2,3,4,5,10"
    S = list(map(lambda x:int(x), S.split(",")))
    second_largest(S)