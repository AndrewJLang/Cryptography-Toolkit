import numpy as np
import math

message = "AJF YYD BZA BAR RJY QKB KXS KNB SOS FQA FSL YFK NOA QQM CSB ZSW YNB FAF EBZ SNL EBZ SIS RRY FHS FKN OJF KNW KJR SBZ SFS KQA RYI SQB NYN LYF KNO JYQ KBK XSK NBS OSF LMB IZY WAF SQ"

message = message.replace(" ", "")

def convertToNum():
    convertedMessage = []
    for x in range(len(message)):
        convertedMessage.append(int(ord(message[x])-65))
    return convertedMessage

message = convertToNum()

messageLength = len(message)

def countLetterFrequency():
    letterCount = np.zeros(26,)
    for x in range(len(message)):
        letterCount[message[x]] += 1
    return letterCount


def ICScore(my_list, listLength):
    squaredNums = [ x**2 for x in my_list ]
    sumNums = sum(squaredNums)
    return (sumNums / (messageLength**2))

print(f"Letter frequencies: {countLetterFrequency()}")

print(f"IC Score: {ICScore(countLetterFrequency(), messageLength)}")