import numpy as np
letterList = []
for x in range(26):
    letterList.append(0)

print(np.array(letterList).shape)

def mostCommonElement(sentence):
    sentence = sentence.replace(" ", "")
    for x in range(len(sentence)):
        index = ord(sentence[x]) - 64
        letterList[index-1] += 1

    print(letterList)
    return letterList.index(max(letterList))+1

# print(mostCommonElement("XDY LYW ENG XDW NKS QWX YBW IYA KGG FMD YYE Y"))

# print(mostCommonElement("TVU VHS WOH ILA PJJ PWO LYZ HYL NYL HAM BU"))

# print(mostCommonElement("HOO NUX PNC WXK BHK XDJ PWW HKG XKS LGX PKZ CSS WHU HGG NSN AXL KDJ MSN CMN PHS NAX PNC WXK B"))

# print(mostCommonElement("GH FJL IOF YJJ TXN YJI HON VHC DJL IOW XFY XXT XON V"))

# word = "HOO"
word = "HOO NUX PNC WXK BHK XDJ PWW HKG XKS LGX PKZ CSS WHU HGG NSN AXL KDJ MSN CMN PHS NAX PNC WXK B"
# word = word.replace(" ", "")

# for x in range(26):
#     newWord = []
#     for i in range(len(word)):
#         newWord.append((ord(word[i])-64-x) % 26)
#     converted = []
#     for x in range(len(newWord)):
#         converted.append(chr(newWord[x]+65))
#     print(converted)

def getValueList(value):
    valueList = []
    for x in range(1,20,1):
        valueList.append(value*x)
    return valueList

valueList = getValueList(18)

def modCalc(vals, breakVal):
    for x in range(len(vals)):
        print(f"Val in List: {valueList[x]}\tMultiple: {x+1}\tMod Value: {int(valueList[x]) % 26}")
        if (int(valueList[x]) % 26) == breakVal:
            break

def multCipher(word):
    word = word.replace(" ", "")
    for i in range(26):
        newWord = []
        for x in range(len(word)):
            newWord.append((ord(word[x])-64-x) % 26)
        converted = []
        for x in range(len(newWord)):
            converted.append(chr(newWord[x]+65))
        print(converted)
        
# multCipher(word)



modCalc(valueList, 6)
