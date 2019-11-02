import numpy as np

#list of potential primitive equations (exponents)
potentialPrimitives = [[1,1,1,1,1], [1,1,0,0,1],[1,0,1,0,1],[1,0,0,1,1]]

degree = 4



def getBaseEquations(deg):
    count = deg**2-1
    divisorList = []
    # for x in range(count):
        # np.zeros
        np.zeros(15)