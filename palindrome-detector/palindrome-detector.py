def main(S):
    S = S.lower()
    word = ''
    for s in S:
        if s.isalnum():
            word += s
    
    reverse_word = ''
    for i in range(len(word)-1, -1, -1):
        reverse_word += word[i]
    
    return word == reverse_word
    

if __name__ == "__main__":
    S = "A man a plan a canal Panama"
    print(main(S))