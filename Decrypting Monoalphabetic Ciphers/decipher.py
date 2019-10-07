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

# valueList = [6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,102,108,114,120,126,132,138,144,150,156,162,168,174,180,186,192,198,204,210,216,222,228,234,240]
valueList = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]

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



modCalc(valueList, 13)
