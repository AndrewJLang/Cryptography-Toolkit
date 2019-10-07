import numpy as np
from collections import Counter

#This program will try and get the key for the encrypted word so that it can decrypt it

# encriptedText = "KFH YYG IGM CEJ SST EBO EUG RWJ TSD VYK ZOZ LIZ KFH XKU UIC WXF WJG AXQ PBQ AGV GXD VDG UEV GMI GYK QQP IPS CLL FYP MUL KFH XPM HGM EVD KAV YQC EGU EAL YYY ZSZ MPX ZOC TXT RIM DID VDG SXO ZFF TSM EDV MEI MDV MPK OUJ KOD UBO AXB OOR SLP ZCW IMD VYG JWM IFQ"
encriptedText = "OHT XAE CUO HEI PGX TIQ HOF YZS TLV CTM JOF AZQ DQD RBF KSY AFA LCX BKK IBA YVC WPP WVP ZHT XWO KSH MZQ CPX TIG TML DTX AEL EBJ VGZ MFY ERX IXA CUQ FMQ ZQC PXY TKW LKK BFT UUM EQO HLT MSF AVI XLR VTB HHT KNN XAH UOL VGG IGH DHP WTK KSN NHV PWQ HPW XLA YJQ PRT LRR YCO HRR OHK SVC CUO ZMQ ZCV CQF ZDB F"

encriptedText = encriptedText.replace(" ", "")

letterFrequency = Counter(encriptedText)
# print(letterFrequency)

mostCommonLetterG = letterFrequency['G']
mostCommonLetterM = letterFrequency['M']

commonDoubleLetters = [[12, 12], [5,5], [19,19], [15,15], [6,6]]

#split into subgroups by matrix size
splitEncrypted = []
a = 1
for x in range(0, len(encriptedText), 2):
    index1 = ord(encriptedText[x]) - 64
    index2 = ord(encriptedText[x+1]) - 64
    splitEncrypted.append([index1, index2])

# key = [[22,15],[24,18]]

def decipherText():
    decipheredCode = []
    for x in range(len(splitEncrypted)):
        decoded = np.matmul(key, splitEncrypted[x])
        decipheredCode.append(decoded)
    
    for x in range(len(decipheredCode)):
        for i in range(len(decipheredCode[x])):
            decipheredCode[x][i] = (decipheredCode[x][i] % 26)
    return decipheredCode

def convertToLetters(message):
    letterText = []
    for x in range(len(message)):
        for i in range(len(message[x])):
            letter = chr(int(message[x][i])+64)
            letterText.append(letter)
    return letterText

print(convertToLetters(decipherText()))


guessPlainTextWord = "THERE"
