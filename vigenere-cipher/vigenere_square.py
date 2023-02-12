import string


LETTERS = list(string.ascii_uppercase)
VIGENERE_SQUARE = [
    LETTERS[n:]+LETTERS[:n]
    for n in range(26)
]