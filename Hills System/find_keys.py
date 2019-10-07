import numpy as np

# encriptedText = "KFH YYG IGM CEJ SST EBO EUG RWJ TSD VYK ZOZ LIZ KFH XKU UIC WXF WJG AXQ PBQ AGV GXD VDG UEV GMI GYK QQP IPS CLL FYP MUL KFH XPM HGM EVD KAV YQC EGU EAL YYY ZSZ MPX ZOC TXT RIM DID VDG SXO ZFF TSM EDV MEI MDV MPK OUJ KOD UBO AXB OOR SLP ZCW IMD VYG JWM IFQ"
encriptedText = "OHT XAE CUO HEI PGX TIQ HOF YZS TLV CTM JOF AZQ DQD RBF KSY AFA LCX BKK IBA YVC WPP WVP ZHT XWO KSH MZQ CPX TIG TML DTX AEL EBJ VGZ MFY ERX IXA CUQ FMQ ZQC PXY TKW LKK BFT UUM EQO HLT MSF AVI XLR VTB HHT KNN XAH UOL VGG IGH DHP WTK KSN NHV PWQ HPW XLA YJQ PRT LRR YCO HRR OHK SVC CUO ZMQ ZCV CQF ZDB F"

#for a=1

encriptedText = encriptedText.replace(" ", "")
commonWord = "THERE" #This must be 5 letters

unitDict = {
    "1" : "1",
    "3" : "9",
    "5" : "21",
    "7" : "15",
    "9" : "3",
    "11": "19",
    "15": "7", 
    "17": "23",
    "19": "11",
    "21": "5",
    "23":"17",
    "25":"25"
}

def convertToNums(encriptedWord, encriptedCommonWord):
    encriptedNums, commonNums = [], []
    for x in range(len(encriptedWord)):
        letter = ord(encriptedWord[x]) - 65
        encriptedNums.append(letter)
    for i in range(len(encriptedCommonWord)):
        letter = ord(encriptedCommonWord[i]) - 65
        commonNums.append(letter)
    
    return encriptedNums, commonNums

convertedText, convertedSearch = convertToNums(encriptedText, commonWord)

def breakDownText(wordCompare, encripted):
    finalDecoded = []
    for x in range(len(encripted)-4):
        evenList = [x,x+1,x+2,x+3,x+4]
        firstTwoEvens = []
        count = 0
        for i in range(len(evenList)):
            if count == 2:
                break
            if evenList[i] % 2 == 0:
                firstTwoEvens.append(evenList[i])
                count += 1

        if evenList[0] % 2 == 0:
            shrinkCompare = np.array(wordCompare[:4])
        else:
            shrinkCompare = np.array(wordCompare[1:])
        
        #decrypted 'guess' message
        shrinkCompare = [[shrinkCompare[0], shrinkCompare[2]], [shrinkCompare[1], shrinkCompare[3]]]

        chosenCipherText = [[encripted[firstTwoEvens[0]], encripted[firstTwoEvens[1]]], [encripted[firstTwoEvens[0]+1], encripted[firstTwoEvens[1]+1]]]

        determinant = np.linalg.det(chosenCipherText) % 26
        detInv = ","
        determinant = round(int(determinant), 5)
        if str(determinant) in unitDict:
            detInv = unitDict[str(determinant)]
        if "," in detInv:
            continue
        detInv = int(detInv)

        flippedMatrix = [[encripted[firstTwoEvens[1]+1], -encripted[firstTwoEvens[1]]], [-encripted[firstTwoEvens[0]+1], encripted[firstTwoEvens[0]]]]
        flippedMatrix = np.array(flippedMatrix)
        invMatrix = detInv*flippedMatrix

        for x in range(len(invMatrix)):
            for i in range(len(invMatrix[x])):
                invMatrix[x][i] = (invMatrix[x][i]%26)

        keyMatrix = np.matmul(shrinkCompare, invMatrix)
        for x in range(len(keyMatrix)):
            for i in range(len(keyMatrix[x])):
                keyMatrix[x][i] = (keyMatrix[x][i]%26)

        plainTextSearch = []
        for x in range(0,len(encripted),2):
            encode = np.matmul(keyMatrix, [encripted[x], encripted[x+1]])
            encode[0] = (encode[0] % 26)
            encode[1] = (encode[1] % 26)
            # if encode[0] == 0:
            #     encode[0] = 26
            # if encode[1] == 0:
            #     encode[1] == 26
            convert0 = chr(int(encode[0]) + 65)
            convert1 = chr(int(encode[1]) + 65)
            plainTextSearch.append([convert0, convert1])
        plainTextSearch = np.array(plainTextSearch)
        plainTextSearch = np.reshape(plainTextSearch, (-1,))
        finalDecoded.append(plainTextSearch)
    return finalDecoded, keyMatrix

answers, key = breakDownText(convertedSearch, convertedText)
plainText = ' '.join(answers[0])
print(plainText)
print(key)