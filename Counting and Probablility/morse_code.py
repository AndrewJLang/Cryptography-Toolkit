import morse

testString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

morseString = morse.string_to_morse(testString)
# print(type(morseString))

stringed = ''.join(morseString)
print(len(stringed))