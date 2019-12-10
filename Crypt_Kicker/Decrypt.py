fileText = open("CKinput04.txt","r")
data = []
key = ("El veloz murciélago hindú comía feliz cardillo y "
        "kiwi cuando la cigüeña tocaba el saxofón detrás del "
        "palenque de paja")
keyLowerCase = key.lower()
keyList = keyLowerCase.split()
keyLength = []
maxLength = 0
indexMaxLength = 0

for index, word in enumerate(keyList):
    if(len(word) > maxLength):
        maxLength = len(word)
        indexMaxLength = index

    keyLength.append(len(word))

'''print(keyLength, " \nmaxLength: ", 
    maxLength, " \nindexMaxLength: ", indexMaxLength)'''

acumulatedString = ''
for index, line in enumerate(fileText):
    if(index > 1):
        if(len(line) > 1 ):
            acumulatedString = acumulatedString + line
        else:
            data.append({"rowData":acumulatedString, "data":acumulatedString.split(), "maxLengthInKey":[], "validKey":[], 
            "encryptedLetters":{}, "isPosibleToDecript":False, "decriptedText":[]})
            acumulatedString = ''

if(len(acumulatedString) > 1):
    data.append({"rowData":acumulatedString, "data":acumulatedString.split(), "maxLengthInKey":[], "validKey":[], 
    "encryptedLetters":{}, "isPosibleToDecript":False, "decriptedText":[]})
    acumulatedString = ''

for case in data:
    for index, word in enumerate(case.get("data")):
        if(len(word) == maxLength and index >= indexMaxLength):
            case.get("maxLengthInKey").append(index - indexMaxLength)

for case in data:
    for matchOfKey in case.get("maxLengthInKey"):
        isValidKey = True
        for index, wordLength in enumerate(keyLength):
            #First if validation to avoyd out of boundaries
            if(len(case.get("data")) <= matchOfKey + index):
                isValidKey = False
            elif(wordLength != len(case.get("data")[matchOfKey + index])):
                isValidKey = False
        if(isValidKey):
            case.get("validKey").append(matchOfKey)

for case in data:
    for validKey in case.get("validKey"):
        if not (case.get("isPosibleToDecript")):
            isValidKey = True
            encryptedLetters = case.get("encryptedLetters")
            encryptedLetters.clear()
            for indexWord, word in enumerate(keyList):
                for indexLetter, letter in enumerate(word):
                    textLetter = case.get("data")[validKey + indexWord][indexLetter]
                    if(encryptedLetters.get(textLetter)):
                        if not (encryptedLetters.get(textLetter) == letter):
                            isValidKey = False
                            '''print("Aqui trono: ", encryptedLetters.get(letter), " ", textLetter)'''
                    else:
                        encryptedLetters.update({textLetter: letter})
            case.update({"isPosibleToDecript": isValidKey})

for case in data:
    if (case.get("isPosibleToDecript")):
        decriptedText = ''
        encryptedLetters = case.get("encryptedLetters")
        for word in case.get("data"):
            decriptedWord = ''
            for textLetter in word:
                decriptedWord = decriptedWord + encryptedLetters.get(textLetter)
            decriptedText = decriptedText + ' ' + decriptedWord
        case.update({'decriptedText': decriptedText.replace(keyLowerCase, '')})

for index, case in enumerate(data, 1):
    print("\n\n          <<<<<<<<<<<<<<<<< ENCRIPTED TEXT", "CASE:", index, ">>>>>>>>>>>>>>>>>>>>>>\n")
    print(case.get("rowData"), "\n")
    if(case.get("isPosibleToDecript")):
        print("          <<<<<<<<<<<< TEXT IS POSSIBLE TO DECODE >>>>>>>>>>>>>>>\n")
        print(case.get("decriptedText"), "\n")
    else:
        print("          <<<<<<<<<< TEXT IS NOT POSSIBLE TO DECODE >>>>>>>>>>>>>\n")
    
