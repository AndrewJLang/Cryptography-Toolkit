import numpy as np
import re

message = "YMI INB CXX YUM MPU EOI XGE IJE ZQH WGN HUQ SHS BIW PQL EQB KWL IJY FPC BKX SXU UZE RQQ HKS GXO RHR HVS PGQ HHP VWB XRV DAZ IEO PIV LVL MKU JYR MAW GIK NBC PIB WUP MYU IKE YYF IST QFM PRE AEP VBY SJV WUV SZQ ARM SYW SMZ ZOW XNF ISV OES RSO EXC PBL YWQ RXY WNH INE TBE LFS LVL SQN FIS VSQ GMP LIJ EVR XCQ LVI FMJ RVL SQG XCW QBD MXV BIC XC"

message = message.replace(" ", "")

print(len(message))

sameWords = ['LVL', 'IJE', 'NBC', 'FISV', 'SQR']

def findOccurances(message, keyword):
    return [i for i in range(len(message)) if message.startswith(keyword, i)]

def findDistances(message, search_list):
    distanceList2, distanceList3 = [], []
    for x in range(len(search_list)):
        lengthList = findOccurances(message, search_list[x])
        # print(f"Word: {search_list[x]}")
        # for i in range(len(lengthList)):
        # print(f"{len(lengthList)}\n")
        if len(lengthList) == 2:
            print(f"Search word length 2: {search_list[x]}")
            distanceList2.append((lengthList[1]-lengthList[0]))
        if len(lengthList) == 3:
            print(f"Search word length 3: {search_list[x]}")
            distanceList3.append((lengthList[1]-lengthList[0]))
            distanceList3.append((lengthList[2]-lengthList[1]))
    return distanceList2, distanceList3

print(findDistances(message, sameWords))