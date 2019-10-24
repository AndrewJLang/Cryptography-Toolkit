import numpy as np
import math

message = "ESP PYR TYP PCE STY VDZ QST DPB FLE TZY DLD LYL AAC ZIT XLE TZY EZC PLW TEJ ESP ASJ DTN TDE EST YVD CPL WTE JTD LYL AAC ZIT XLE TZY EZS TDP BFL ETZ YDE SPX LES PXL ETN TLY OZP DYE NLC P"

message = message.replace(" ", "")

def convertToNumWithArg(word):
    convertedMessage = []
    for x in range(len(word)):
        convertedMessage.append(int(ord(word[x])-65))
    return convertedMessage

def convertToNum():
    convertedMessage = []
    for x in range(len(message)):
        convertedMessage.append(int(ord(message[x])-65))
    return convertedMessage

message = convertToNum()

messageLength = len(message)

print(messageLength)

def countLetterFrequency(letter_list):
    letterCount = np.zeros(26,)
    for x in range(len(letter_list)):
        letterCount[letter_list[x]] += 1
    return letterCount

def countLetterFrequencyNoArg():
    letterCount = np.zeros(26,)
    for x in range(len(message)):
        letterCount[message[x]] += 1
    return letterCount

def ICScore(my_list, listLength):
    squaredNums = [ x**2 for x in my_list ]
    sumNums = sum(squaredNums)
    return (sumNums / (messageLength**2))

print(f"Letter frequencies: {countLetterFrequencyNoArg()}")

print(f"IC Score: {ICScore(countLetterFrequencyNoArg(), messageLength)}")