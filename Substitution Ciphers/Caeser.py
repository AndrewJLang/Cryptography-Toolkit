def caeser(text, shift):
    if shift > 26:
        shift -= 26
    elif shift < 0:
        shift += 26
    ciphered = ""
    for letter in text:
        shifted = ord(letter) + shift
        if 65 <= shifted <= 90 or 97 <= shifted <= 122:
            ciphered += chr(shifted)
        else:
            ciphered += chr(shifted - 26)

    print(ciphered)
