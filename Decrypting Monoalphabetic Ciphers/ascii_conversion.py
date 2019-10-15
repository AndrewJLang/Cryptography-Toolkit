import numpy as np

def stripSpaces(message):
    message = message.replace(" ", "")
    return message

def convertUpperCase(message):
    convertedMessage = []
    for x in range(len(message)):
        convertedMessage.append(int(ord(message[x])-65))
    return convertedMessage

def convertToText(num_list):
    convertedList = []
    for x in range(len(num_list)):
        convertedList.append(chr(num_list[x]+64))
    convertedList = ''.join(convertedList)
    return convertedList