import numpy as np
import argparse as ap

keyword = "super"
startValue = 0 #for whether a=0 or a=1

encodedMessage = "AZX LRV USS CDU GJF JYK IIQ GTW JSA TMY SPT HVU LNT KWX XAF MFS LRN YPX CWU HXR VIA PRJ"

encodedMessage = encodedMessage.replace(" ", "")

def convertToNum():
    convertedText = []
    for x in range(len(encodedMessage)):
        convertedText.append(ord(encodedMessage[x])-64 + startValue)
    return convertedText

encodedMessage = convertToNum()

def decryptMessage():
    for x in range(len(encodedMessage)):
        
