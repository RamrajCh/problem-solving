from vigenere_square import LETTERS, VIGENERE_SQUARE

def vigenere_cipher(plaintext, keyword):
    # Keyword is repeated to match the length of the message
    M = len(plaintext)
    N = len(keyword)
    keyword = keyword * (M//N) + keyword[:M%N]
    
    print(f"plaintext = {plaintext}")
    print(f"keyword = {keyword}")
    
    # Encryption
    encrypted = ''
    for i in range(M):
        plaintext_letter = plaintext[i]
        keyword_letter = keyword[i]
        j = LETTERS.index(plaintext_letter)
        k = LETTERS.index(keyword_letter)
        
        encrypted += VIGENERE_SQUARE[k][j]
    print(f"encrypted = {encrypted}")
    
    # Decryption
    decrypted = ''
    for i in range(len(encrypted)):
        encrypted_letter = encrypted[i]
        keyword_letter = keyword[i]
        j = LETTERS.index(keyword_letter)
        k = VIGENERE_SQUARE[j].index(encrypted_letter)
        
        decrypted += LETTERS[k]
        
    print(f"decrypted = {decrypted}")
        

if __name__ == "__main__":
    plaintext = "THISISATOPSECRETMESSAGE"
    keyword = "HELLO"
    vigenere_cipher(plaintext, keyword)