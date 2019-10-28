import numpy as np

moduloN = 26

f = open("plaintext.txt","w+")
l = open("shithole.txt","w+")

def decipherHill(sentence, invKey, a=1):
    sentence = sentence.replace(" ", "")
    decipheredText = []
    for x in range(0, len(sentence), 2):
        groupedCipher = [0,0]
        index1 = ord(sentence[x]) - 65 + a
        index2 = ord(sentence[x+1]) - 65 + a
        groupedCipher[0] = index1
        groupedCipher[1] = index2
        deciphered = np.matmul(invKey, groupedCipher)
        translated = []
        for x in range(len(deciphered)):
            translated.append((deciphered[x]%moduloN))
        decipheredText.append(translated)
    return decipheredText

decipherWord = "YMAWABGYAWKYYUWJSNYMCZ"

keysAndText = []

validKeys = []

def convertToLetter(numList):
    newStr = []
    for x in range(len(numList)):
        newStr.append(chr(int(numList[x]) + 65))
    return newStr

def decipher(key):

    det = np.linalg.det(key) % moduloN

    if (det == 0):
        return

    invKey = np.zeros((2,2))

    for x in range(len(key)):
        for i in range(len(key[x])):
            invKey[x][i] = ((key[x][i]* det)% moduloN)

    decipheredNumText = decipherHill(decipherWord, invKey)

    decipheredNumText = np.array(decipheredNumText)
    numText = np.reshape(decipheredNumText, (-1,))

    plainText = convertToLetter(numText)
    plainText = ' '.join(plainText)

    string = "" + str(key)[1:-1] + "\n"  + plainText + "\n"
    print(string)
    keysAndText.append([key, plainText])

key = [[17, 24], [21, 3]]

# decipher(key)

for x1 in range(26):
    for x2 in range(26):
        for x3 in range(26):
            for x4 in range(26):
                decipher([[x1, x2], [x3, x4]])

for i in range(len(keysAndText)):
    if keysAndText[i][0][0][0] > 9:
        validKeys.append(keysAndText[i])
    elif keysAndText[i][0][0][1] > 9:
        validKeys.append(keysAndText[i])
    elif keysAndText[i][0][1][0] > 9:
        validKeys.append(keysAndText[i])
    elif keysAndText[i][0][1][1] > 9:
        validKeys.append(keysAndText[i][1])

l.write(str(keysAndText))

for elem in validKeys:
    f.write(elem[1] + "\n")
