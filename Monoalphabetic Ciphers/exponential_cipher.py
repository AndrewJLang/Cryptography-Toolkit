import numpy as np

#Problem #3 Encryption

encriptList = [8, 15, 23, 1, 18, 5, 25, 15, 21]
moduloN = 26
encryptedList = []
for x in range(len(encriptList)):
    encryptedList.append((encriptList[x]**5) % moduloN)

# print(encryptedList)

affineList = [9, 5, 1, 20, 3, 8, 5, 5, 19, 5]
affineEncrypted = []
for x in range(len(affineList)):
    affineEncrypted.append((affineList[x]*3 + 8) % moduloN)

# print(affineEncrypted)

for x in range(1,27):
    print(f"Term: {x}\tExponentiated: {(x**5)%26}")