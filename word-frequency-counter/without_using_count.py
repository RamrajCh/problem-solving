def word_count(S):
    import re
    regex = r"[^a-z]"
    
    S = S.lower()
    words = list(map(lambda x: re.sub(regex, '', x), S.split()))
    
    freq = {}
    
    for word in words:
        if not word in freq.keys():
            freq[word] = 0
        freq[word] += 1

    print(freq)

if __name__ == "__main__":
    S = input()
    word_count(S)