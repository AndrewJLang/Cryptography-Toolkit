import numpy as np
import math

message = "YBR GPT OOY CBC GUG SNR TCW MVF RMU GJC MUI RCC UZV LJX BAJ DNU RTJ LLF KFF YBL JMZ NWG YNY JYB RRV HCG VLL MGH DKB NCN JHF NRW YNY JDV VTL ZGO RPX IAR QBY PNL YYI RLG YTV LYI GUG SEN OMZ NVA YSS IRP DXR SGS CGR UFS BHP GLN VLX BNI CJP BYT JXG BEJ NHF MZN BSR MYE NGS ZVA BBB REC YBR OCW LVR QFL RNL IER RNZ MSE MRA RGR NHT XGQ FRQ MZL OEY NHF QGI HBG CAI YIC YIU RJU OFT PFM CEC FFY LJF LTR LZG ORP XIE GMQ IBX YYN UVL LMV AYM OAQ PJX GUM ZMN ABI CZR LXC BAQ"

message = message.replace(" ", "")

def convertToNumWithArg(word):
    convertedMessage = []
    for x in range(len(word)):
        convertedMessage.append(int(ord(word[x])-65))
    return convertedMessage

def convertToNum():
    convertedMessage = []
    for x in range(len(message)):
        convertedMessage.append(int(ord(message[x])-65))
    return convertedMessage

message = convertToNum()

messageLength = len(message)

print(messageLength)

def countLetterFrequency(letter_list):
    letterCount = np.zeros(26,)
    for x in range(len(letter_list)):
        letterCount[letter_list[x]] += 1
    return letterCount

def countLetterFrequencyNoArg():
    letterCount = np.zeros(26,)
    for x in range(len(message)):
        letterCount[message[x]] += 1
    return letterCount

def ICScore(my_list, listLength):
    squaredNums = [ x**2 for x in my_list ]
    sumNums = sum(squaredNums)
    return (sumNums / (messageLength**2))

# print(f"Letter frequencies: {countLetterFrequencyNoArg()}")

# print(f"IC Score: {ICScore(countLetterFrequencyNoArg(), messageLength)}")