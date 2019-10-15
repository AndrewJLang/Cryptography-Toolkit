import numpy as np
import ascii_conversion

message = "AJF YYD BZA BAR RJY QKB KXS KNB SOS FQA FSL YFK NOA QQM CSB ZSW YNB FAF EBZ SNL EBZ SIS RRY FHS FKN OJF KNW KJR SBZ SFS KQA RYI SQB NYN LYF KNO JYQ KBK XSK NBS OSF LMB IZY WAF SQ"

message = ascii_conversion.stripSpaces(message)

message = ascii_conversion.convertUpperCase(message)
print(message)

def affineFunc(aInv,b,val):
    val = val + 1
    return (((val*aInv)-b) % 26)


def decryptedMessage(text):
    decrypted = []
    for x in range(len(text)):
        decrypted.append(affineFunc(19, 18, text[x]))
    return ascii_conversion.convertToText(decrypted)

print(decryptedMessage(message))