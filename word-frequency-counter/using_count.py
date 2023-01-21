def word_count(S):
    import re
    regex = r"[^a-z]"
    
    S = S.lower()
    words = list(map(lambda x: re.sub(regex, '', x), S.split()))
    
    freq = {}
    
    for word in words:
        if not word in freq.keys():
            c = words.count(word)
            freq[word] = c

    print(freq)

if __name__ == "__main__":
    standard_input = "This is a test. This is only a test."
    S = input()
    word_count(S)