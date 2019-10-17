import numpy as np
import re

message = "YBR GPT OOY CBC GUG SNR TCW MVF RMU GJC MUI RCC UZV LJX BAJ DNU RTJ LLF KFF YBL JMZ NWG YNY JYB RRV HCG VLL MGH DKB NCN JHF NRW YNY JDV VTL ZGO RPX IAR QBY PNL YYI RLG YTV LYI GUG SEN OMZ NVA YSS IRP DXR SGS CGR UFS BHP GLN VLX BNI CJP BYT JXG BEJ NHF MZN BSR MYE NGS ZVA BBB REC YBR OCW LVR QFL RNL IER RNZ MSE MRA RGR NHT XGQ FRQ MZL OEY NHF QGI HBG CAI YIC YIU RJU OFT PFM CEC FFY LJF LTR LZG ORP XIE GMQ IBX YYN UVL LMV AYM OAQ PJX GUM ZMN ABI CZR LXC BAQ"

message = message.replace(" ", "")

sameWords = ['GUGS', 'YNYJ', 'YBR', 'RPXI', 'JXG', 'NHF', 'MZN', 'FFY']

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