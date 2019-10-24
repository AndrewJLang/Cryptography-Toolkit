import numpy as np
import ascii_conversion

# message = "YBR GPT OOY CBC GUG SNR TCW MVF RMU GJC MUI RCC UZV LJX BAJ DNU RTJ LLF KFF YBL JMZ NWG YNY JYB RRV HCG VLL MGH DKB NCN JHF NRW YNY JDV VTL ZGO RPX IAR QBY PNL YYI RLG YTV LYI GUG SEN OMZ NVA YSS IRP DXR SGS CGR UFS BHP GLN VLX BNI CJP BYT JXG BEJ NHF MZN BSR MYE NGS ZVA BBB REC YBR OCW LVR QFL RNL IER RNZ MSE MRA RGR NHT XGQ FRQ MZL OEY NHF QGI HBG CAI YIC YIU RJU OFT PFM CEC FFY LJF LTR LZG ORP XIE GMQ IBX YYN UVL LMV AYM OAQ PJX GUM ZMN ABI CZR LXC BAQ"
message = "ESP PYR TYP PCE STY VDZ QST DPB FLE TZY DLD LYL AAC ZIT XLE TZY EZC PLW TEJ ESP ASJ DTN TDE EST YVD CPL WTE JTD LYL AAC ZIT XLE TZY EZS TDP BFL ETZ YDE SPX LES PXL ETN TLY OZP DYE NLC P"

message = ascii_conversion.stripSpaces(message)

message = ascii_conversion.convertUpperCase(message)
# print(message)

def affineFunc(aInv,b,val):
    val = val + 1
    return (((val*aInv)-b) % 26)

def decryptionCalc(aInv,b,val):
    return ((val-b)*aInv) % 26

def properDecryption(aInv, b, val):
    return ((val-b) % 26)

def decryptedMessage(text):
    decrypted = []
    for x in range(len(text)):
        # decrypted.append(decryptionCalc(1,11,text[x]))
        # decrypted.append(affineFunc(1,11,text[x]))
        decrypted.append(properDecryption(1,11,text[x]))
    return ascii_conversion.convertToText(decrypted)

print(decryptedMessage(message))