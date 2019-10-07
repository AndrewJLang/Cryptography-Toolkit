import numpy as np

def encipherText(sentence, cipherKey, a=0):
    sentence = sentence.replace(" ", "")
    encipheredText = []
    for x in range(0, len(sentence), 2):
        groupedCipher = [0, 0]
        index1 = ord(sentence[x]) - 97 + a
        index2 = ord(sentence[x+1]) - 97 + a
        groupedCipher[0] = index1
        groupedCipher[1] = index2
        enciphered = np.matmul(cipherKey, groupedCipher)
        translated = []
        for x in range(len(enciphered)):
            translated.append((enciphered[x]%26))
        encipheredText.append(translated)
    return encipheredText

encipherWord = "so long and thanks for all the fish"
key = [[6,3],[7,8]]

print(encipherText(encipherWord, key))