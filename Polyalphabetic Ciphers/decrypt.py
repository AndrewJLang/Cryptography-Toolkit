import numpy as np
import argparse as ap

keyword = "QUEEN"
startValue = 0 #for whether a=0 or a=1

encodedMessage = "YMI INB CXX YUM MPU EOI XGE IJE ZQH WGN HUQ SHS BIW PQL EQB KWL IJY FPC BKX SXU UZE RQQ HKS GXO RHR HVS PGQ HHP VWB XRV DAZ IEO PIV LVL MKU JYR MAW GIK NBC PIB WUP MYU IKE YYF IST QFM PRE AEP VBY SJV WUV SZQ ARM SYW SMZ ZOW XNF ISV OES RSO EXC PBL YWQ RXY WNH INE TBE LFS LVL SQN FIS VSQ GMP LIJ EVR XCQ LVI FMJ RVL SQG XCW QBD MXV BIC XC"

encodedMessage = encodedMessage.replace(" ", "")

def convertToNum():
    convertedText, convertedKeyword = [], []
    for x in range(len(encodedMessage)):
        convertedText.append(ord(encodedMessage[x])-65 + startValue)
    for x in range(len(keyword)):
        convertedKeyword.append(ord(keyword[x])-65 + startValue)
    return convertedText, convertedKeyword

encodedMessage, keyword = convertToNum()

def decryptWord():
    count = 0
    newMessage = []
    for x in range(len(encodedMessage)):
        if count % 5 == 0:
            newMessage.append((encodedMessage[x] + keyword[0]) % 26)
        if count % 5 == 1:
            newMessage.append((encodedMessage[x] + keyword[1]) % 26)
        if count % 5 == 2:
            newMessage.append((encodedMessage[x] + keyword[2]) % 26)
        if count % 5 == 3:
            newMessage.append((encodedMessage[x] + keyword[3]) % 26)
        if count % 5 == 4:
            newMessage.append((encodedMessage[x] + keyword[4]) % 26)
        count += 1
    return newMessage

plaintext = decryptWord()

def convertToText(num_list):
    convertedList = []
    for x in range(len(num_list)):
        convertedList.append(chr(num_list[x]+65))
    convertedList = ''.join(convertedList)
    return convertedList

print(convertToText(plaintext))