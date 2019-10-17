import numpy as np
import math

message = "OTG WRV RHU GXO XUQ UEK VYO TSE NYU NSI YSH MHB BUR ZTR CCD DAK MHC ALI OJZ UOT JYC KFN KIO THO GWK Z"

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