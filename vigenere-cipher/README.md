# Vigenère Cipher
## Problem Statement
Implement a Vigenère cipher algorithm in Python that can be used to encrypt and decrypt messages.

## Example

`plaintext = THISISATOPSECRETMESSAGE`

`keyword = HELLOHELLOHELLOHELLOHEL`

`encrypted = ALTDWZEEZDZINCSAQPDGHKP`

`decrypted = THISISATOPSECRETMESSAGE`

## About the Vigenère Cipher
The Vigenère cipher is a method of encrypting messages by using a series of interwoven Caesar ciphers, based on the letters of a keyword. Each letter in the message is shifted by a number of places based on its corresponding letter in the keyword.

The Vigenère cipher is considered to be more secure than a single Caesar cipher, as it uses a different shift value for each letter in the message. This makes it more difficult to crack the code, as the frequency analysis used to break a Caesar cipher is not effective against a Vigenère cipher.

## Vigenère Cipher Algorithm

1. The first step is to create a Vigenère square, also known as a tabula recta, which is a table of alphabets with each row shifted one place to the left from the previous row.

2. The keyword is repeated as many times as necessary to match the length of the message.

3. For each letter in the message, its corresponding letter in the keyword is found and its corresponding row in the Vigenère square is used to encrypt the letter.

4. To decrypt the message, the process is reversed, with the corresponding row in the Vigenère square being found using the keyword and the original letter being found by moving left instead of right.

This is wikipedia link for the [Vigenère Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).