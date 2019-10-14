import numpy as np
import math

message = "TWV CFJ FAH XOC PBH ZMH ZZQ BUX SXI DLH VSZ RFX YIG KMZ ZHW GLQ QMO IQF RFK HVM KLQ GIC HYI IXS PCI HQK PRU GVU GJM DCI FAL VSZ WME VAS JXZ HUM BKI DXZ XWE KBH ZMH ZZQ BUX SXI DUB XVV CFA HXG GVQ MAC WEX QKL WHZ RST JSB KVM WPG HZS Z"

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

print(ICScore(countLetterFrequency(), messageLength))