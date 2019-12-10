testFile = open("Test_2.txt", "r")
countryA = []
countryB = []
xIsInA = False
yIsInA = False
xIsInB = False
yIsInB = False

def getNumbers(line):
    numbers = []
    for number in line.split():
        numbers.append(int(number))
    return numbers

def findIfAlreadyAdded(x, y):
    global xIsInA, yIsInA, xIsInB, yIsInB
    xIsInA = x in countryA
    yIsInA = y in countryA
    xIsInB = x in countryB
    yIsInB = y in countryB

def setFriends(x, y):
    if(not xIsInA and not yIsInA and not xIsInB and not yIsInB):
        countryA.append(x)
        countryA.append(y)
    elif(xIsInA):
        if(not yIsInA and not yIsInB):
            countryA.append(y)
        elif(yIsInB):
            print(-1)
    elif(xIsInB):
        if(not yIsInA and not yIsInB):
            countryB.append(y)
        elif(yIsInA):
            print(-1)
    elif(yIsInA):
        if(not xIsInA and not xIsInB):
            countryA.append(x)
        elif(xIsInB):
            print(-1)
    elif(yIsInB):
        if(not xIsInA and not xIsInB):
            countryB.append(x)
        elif(xIsInA):
            print(-1)
        

def setEnemies(x, y):
    if(not xIsInA and not yIsInA and not xIsInB and not yIsInB):
        countryA.append(x)
        countryB.append(y)
    elif(xIsInA):
        if(not yIsInA and not yIsInB):
            countryB.append(y)
        elif(yIsInA):
            print(-1)
    elif(xIsInB):
        if(not yIsInA and not yIsInB):
            countryA.append(y)
        elif(yIsInB):
            print(-1)
    elif(yIsInA):
        if(not xIsInA and not xIsInB):
            countryB.append(x)
        elif(xIsInA):
            print(-1)
    elif(yIsInB):
        if(not xIsInA and not xIsInB):
            countryA.append(x)
        elif(xIsInB):
            print(-1)

def areFriends(x, y):
    comparison(x, y, 1, 0)

def areEnemies(x, y):
    comparison(x, y, 0, 1)

def comparison(x, y, same, different):
    if((not xIsInA and not xIsInB) or (not yIsInA and not yIsInB)):
        print(0)
    elif(xIsInA):
        if(yIsInB):
            print(different)
        elif(yIsInA):
            print(same)
    elif(xIsInB):
        if(yIsInA):
            print(different)
        elif(yIsInB):
            print(same)
    elif(yIsInA):
        if(xIsInB):
            print(different)
        elif(xIsInA):
            print(same)
    elif(yIsInB):
        if(xIsInA):
            print(different)
        elif(xIsInB):
            print(same)
 

for line in testFile:
    numbers = getNumbers(line)
    if(numbers):
        if(len(numbers) == 1):
            print("=================== STARTING NEW COUNT ==================")
        elif(numbers[0] > 0 ):
            findIfAlreadyAdded(numbers[1], numbers[2])
            print("Line:", numbers)
            if(numbers[0] == 1):
                setFriends(numbers[1], numbers[2])
            elif(numbers[0] == 2):
                setEnemies(numbers[1], numbers[2])
            elif(numbers[0] == 3):
                areFriends(numbers[1], numbers[2])
            elif(numbers[0] == 4):
                areEnemies(numbers[1], numbers[2])
        elif(numbers[0] == 0 ):
            print("A", countryA)
            print("B", countryB)
            countryA = []
            countryB = []
        









