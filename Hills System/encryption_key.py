import numpy as np
from textwrap import wrap
from scipy import *

#a=0
def convertUpperCase(message):
    convertedMessage = []
    for x in range(len(message)):
        convertedMessage.append(int(ord(message[x])-65))
    return convertedMessage

#a=0
def convertToText(num_list):
    convertedList = []
    for x in range(len(num_list)):
        convertedList.append(chr(num_list[x]+65))
    convertedList = ''.join(convertedList)
    return convertedList

plaintext = "EASYCHEESYSQUEEZYPEAS"
ciphertext = "YMAWABGYAWKYYUWJSNYMCZ"

plaintext = convertUpperCase(plaintext)
ciphertext = convertUpperCase(ciphertext)

print(plaintext)
print(ciphertext)

#solving for encryption key
def getKey(plain, cipher):
    aList, bList, cList, dList = [], [], [], []
    for x in range(len(plain),step=2):
        a,b = symbols(['a', 'b'])
        sol = solve(plain[x]*a + plain[x+1]*b = cipher[x], [a,b])
        print(sol)


getKey(plaintext, ciphertext)
