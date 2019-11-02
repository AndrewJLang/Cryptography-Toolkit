import numpy as np

#list of potential primitive equations (exponents)
potentialPrimitives = [[1,1,1,1,1], [1,1,0,0,1],[1,0,1,0,1],[1,0,0,1,1]] #degree 4 irreducible equations
# potentialPrimitives = [[1,1,0,1], [1,0,1,1]] #degree 3 irreducible equations

degree = 4

print(np.array(potentialPrimitives).shape)

def getBaseEquations(deg):
    count = deg**2
    divisorList = []
    for x in range((deg+1),count):
        tempList = np.zeros(16)
        tempList[x] = 1
        tempList[0] = 1
        divisorList.append(tempList)
    return divisorList

divisors = getBaseEquations(degree)

def checkRemainder():
    for x in range(len(potentialPrimitives)):
        Y = np.array(potentialPrimitives[x])  
        print(f"potential: {potentialPrimitives[x]}")
        for i in range(len(divisors)):
            X = np.array(divisors[i])
            quotient, remainder = np.polydiv(X, Y)
            for j in range(len(remainder)):
                remainder[j] = (remainder[j] % 2)
            print(remainder)

checkRemainder()        