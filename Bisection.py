def isIn(char, aStr):
    wordFound == False
    wordLength = int(len(aStr) / 2)
    if aStr[wordLength] == char:
        wordFound == True
        return wordFound
    else:
        while wordFound == False:
            if ord(aStr[wordLength]) > ord(char):
                wordLength - 1
            elif ord(aStr[wordLength]) < ord(char):
                wordLength + 1
            elif ord(aStr[wordLength]) == ord(char):
                wordFound = True
                return wordFound




print(isIn("s", "abcdefghijkl"))
