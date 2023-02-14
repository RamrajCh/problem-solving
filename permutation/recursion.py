def _permutation(S):
    result = []
    permutation(S, 0, result)
    print(result)
    
    
def permutation(data, i, result):
    if i == len(data):
        result.append(list(data))
    
    for j in range(i, len(data)):
        data[j], data[i] = data[i], data[j]
        permutation(data, i+1, result)
        data[j], data[i] = data[i], data[j]
        

if __name__ == "__main__":
    S = [1,2,3]
    _permutation(S)