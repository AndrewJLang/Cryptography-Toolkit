# Cryptography-Toolkit
Toolkit for cryptography problems implemented in python

### All messages are encrypted/decrypted in Z26 (mod 26)

## Counting and Probability
 - morse_code.py
   - counts the amount of characters needed if English message is translated to morse code

## Decrypting Monoalphabetic Ciphers
 - ascii_conversion.py
   - Helper method for converting numbers to letters and vice versa
 - decipher.py
   - Can find the most common element/character in a string and return each characters number of occurances
   - Implementation of an exponential cipher
 - decrypt_affine.py
   - Decryption for affine cipher given alpha and beta values

## Hills System
  #### Note all encryption/decryption is for 2x2 key matrix
  - find_keys.py
    - Runs through the different options for finding the key of a message encrypted using hills cipher
    - Takes a 5 letter word that user believes will appear within the text
  - hill_decipher.py
    - deciphers a hills system encrypted message given the key is already know
  - hill_encipher.py
    - enciphers a message with the a given key

## Monoalphabetic Ciphers
  - encoded_message.py
    - encodes a message using a multiplicative key (multiplicative cipher)
  - exponential_cipher.py
    - Encodes with exponential and affine ciphers (separate)
  - unit_mult.py
    -Finds the values of two units in Z26 multiplied together

## Polyalphabetic Ciphers
  - IC_score.py
    - calculates the IC score of a string to help decide if it is monoalphabetic or polyalphabetic

## Substitution Ciphers
  - Caeser.py
    - A cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
  - A1Z26.py
    - A cipher where each alphabet letter is replaced by its number in the alphabet.
## Set Theory, Integers Modulo n and Rings and Fields
  - OneToOne.py
    - Tests to see if an encryption method (exponential or multiplicative) has one-to-one correlation
 
