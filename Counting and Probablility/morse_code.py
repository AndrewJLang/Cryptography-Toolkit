import morse

testString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

morseString = morse.string_to_morse(testString)

allSingleCount = ''.join(morseString)

countProperValues = 0
for x in range(len(allSingleCount)):
    if allSingleCount[x] == '-':
        print("hit")
        countProperValues += 3
    else:
        countProperValues += 1

print(f"Length where everything is equal: {len(allSingleCount)}")
print(f"Length where dash is length 3: {countProperValues}")