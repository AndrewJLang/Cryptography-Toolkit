import numpy as np

moduloN = 26

def decipherHill(sentence, invKey, a=0):
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

# decipherWord = "MUB YAQ IQG NAE WOS RZQ JIR ZQK CLI ZAG SXC JAA QFR MHO"
decipherWord = "OHT XAE CUO HEI PGX TIQ HOF YZS TLV CTM JOF AZQ DQD RBF KSY AFA LCX BKK IBA YVC WPP WVP ZHT XWO KSH MZQ CPX TIG TML DTX AEL EBJ VGZ MFY ERX IXA CUQ FMQ ZQC PXY TKW LKK BFT UUM EQO HLT MSF AVI XLR VTB HHT KNN XAH UOL VGG IGH DHP WTK KSN NHV PWQ HPW XLA YJQ PRT LRR YCO HRR OHK SVC CUO ZMQ ZCV CQF ZDB F"
key = [[3,5],[4,5]]


# key = [[5, -2], [-8, 3]]
det = np.linalg.det(key) % moduloN
invKey = np.zeros((2,2))

for x in range(len(key)):
    for i in range(len(key[x])):
        invKey[x][i] = ((key[x][i]* det)% moduloN)

decipheredNumText = decipherHill(decipherWord, invKey)
print(np.array(decipheredNumText))

decipheredNumText = np.array(decipheredNumText)
numText = np.reshape(decipheredNumText, (-1,))

def convertToLetter(numList):
    newStr = []
    for x in range(len(numList)):
        newStr.append(chr(int(numList[x]) + 64))
    return newStr

plainText = convertToLetter(numText)

plainText = ' '.join(plainText)
print(plainText)