import numpy as np

encrypted = "YMAWABGYAWKYYUWJSNYM"
plaintext = "EASYCHEESYSQUEEZYPEA"

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

ciphertext = convertUpperCase(encrypted)
plaintext = convertUpperCase(plaintext)
print(ciphertext)

def decode(x1,x2,x3,x4,text):
    key = [[x1, x2], [x3,x4]]
    decrypted = []
    x = 0
    while (x < len(text)):
        pos1 = text[x]
        pos2 = text[x+1]
        plainFirst = (((x1*pos1)+(x2*pos2)) % 26)
        plainSecond = (((x3*pos1)+(x4*pos2)) % 26)
        decrypted.append(plainFirst)
        decrypted.append(plainSecond)
        x = x + 2
    print(decrypted)

for x in range(26): #a
    for x2 in range(26): #b
        for x3 in range(26): #c
            for x4 in range(26): #d
                decoded = decode(x, x2, x3, x4, ciphertext)
                if decoded == plaintext:
                    print(f"Decoding key: [{x},{x2}] [{x3}, {x4}]")