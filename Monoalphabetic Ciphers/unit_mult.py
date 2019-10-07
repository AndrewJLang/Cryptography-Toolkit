import numpy as np

units = [1,3,5,7,9,11,15,17,19,21,23,25]

for x in range(len(units)):
    for i in range(len(units)):
        print(f"{units[x]}\t{units[i]}\t modulo: {(units[x]*units[i])%26}")

