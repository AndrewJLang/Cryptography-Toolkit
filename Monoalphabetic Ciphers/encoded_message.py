import numpy as np

#write this all in lowercase
textMessage = "this is my test string. it may not be that tricky to figure out."

moduloN = 26

convertedList = [ord(x) for x in textMessage]

for x in range(len(convertedList)):
    convertedList[x] = convertedList[x] - 96

# print(convertedList)

#I just use the multiplication cipher, write a different method if you want to use something else
def encodeText(multCipher):
    finalEncoding = []
    newString = []
    for x in range(len(convertedList)):
        if convertedList[x] > 0:
            finalEncoding.append((convertedList[x]*multCipher) % moduloN)
        elif convertedList[x] == -64: #This is if it is a space
            finalEncoding.append(-2)
        elif convertedList[x] == -50: #This is if it is a period
            finalEncoding.append(-1)
    for x in range(len(finalEncoding)):
        if finalEncoding[x] > 0:
            newString.append(chr(finalEncoding[x] + 96))
        elif finalEncoding[x] == -2:
            newString.append(" ")
        elif finalEncoding[x] == -1:
            newString.append(".")
    return newString

print(encodeText(7))