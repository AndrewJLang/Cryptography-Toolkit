import numpy as np
import IC_score

message = "YBR GPT OOY CBC GUG SNR TCW MVF RMU GJC MUI RCC UZV LJX BAJ DNU RTJ LLF KFF YBL JMZ NWG YNY JYB RRV HCG VLL MGH DKB NCN JHF NRW YNY JDV VTL ZGO RPX IAR QBY PNL YYI RLG YTV LYI GUG SEN OMZ NVA YSS IRP DXR SGS CGR UFS BHP GLN VLX BNI CJP BYT JXG BEJ NHF MZN BSR MYE NGS ZVA BBB REC YBR OCW LVR QFL RNL IER RNZ MSE MRA RGR NHT XGQ FRQ MZL OEY NHF QGI HBG CAI YIC YIU RJU OFT PFM CEC FFY LJF LTR LZG ORP XIE GMQ IBX YYN UVL LMV AYM OAQ PJX GUM ZMN ABI CZR LXC BAQ"

message = message.replace(" ", "")

keywordLength = 5

col1List, col2List, col3List, col4List, col5List = [], [], [], [], []

def calcFreq():
    for x in range(len(message)):
        if x % 5 == 0:
            col1List.append(message[x])
        if x % 5 == 1:
            col2List.append(message[x])
        if x % 5 == 2:
            col3List.append(message[x])
        if x % 5 == 3:
            col4List.append(message[x])
        if x % 5 == 4:
            col5List.append(message[x])

calcFreq()

col1Joined = "".join(col1List)
col2Joined = "".join(col2List)
col3Joined = "".join(col3List)
col4Joined = "".join(col4List)
col5Joined = "".join(col5List)

col1Num = IC_score.convertToNumWithArg(col1Joined)
col2Num = IC_score.convertToNumWithArg(col2Joined)
col3Num = IC_score.convertToNumWithArg(col3Joined)
col4Num = IC_score.convertToNumWithArg(col4Joined)
col5Num = IC_score.convertToNumWithArg(col5Joined)

col1Freq = IC_score.countLetterFrequency(col1Num)
col2Freq = IC_score.countLetterFrequency(col2Num)
col3Freq = IC_score.countLetterFrequency(col3Num)
col4Freq = IC_score.countLetterFrequency(col4Num)
col5Freq = IC_score.countLetterFrequency(col5Num)

print(f"Col 1 letter freq: {col1Freq}\n")
print(f"Col 2 letter freq: {col2Freq}\n")
print(f"Col 3 letter freq: {col3Freq}\n")
print(f"Col 4 letter freq: {col4Freq}\n")
print(f"Col 5 letter freq: {col5Freq}\n")

col1Max = list(col1Freq).index(max(col1Freq))
col2Max = list(col2Freq).index(max(col2Freq))
col3Max = list(col3Freq).index(max(col3Freq))
col4Max = list(col4Freq).index(max(col4Freq))
col5Max = list(col5Freq).index(max(col5Freq))

print(f"Col 1 max Index: {col1Max}\t Value: {max(col1Freq)}")
print(f"Col 2 max Index: {col2Max}\t Value: {max(col2Freq)}")
print(f"Col 3 max Index: {col3Max}\t Value: {max(col3Freq)}")
print(f"Col 4 max Index: {col4Max}\t Value: {max(col4Freq)}")
print(f"Col 5 max Index: {col5Max}\t Value: {max(col5Freq)}")