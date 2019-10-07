import numpy as np

fieldSize = 26
numArray = np.arange(26)
testK = 3

#This is for the a**k problem (power problem)
sameValuesPower = []
for x in range(len(numArray)):
    sameValuesPower.append((numArray[x]**testK) % fieldSize)

# print(sameValuesPower)

#This is for the a*k problem (multiplication problem)
sameValuesMult = []
for x in range(len(numArray)):
    sameValuesMult.append((numArray[x] * testK) % fieldSize)

print(sameValuesMult)