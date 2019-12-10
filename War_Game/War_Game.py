import re

## Test_Original War_Game_datos_prueba02
testFile = open("Test_Original.txt", "r")
graph = {}
visited = []
xIsInGraph = False
yIsInGraph = False
areFriends = 0
areEnemies = 0


def getNumbers(line):
    numbers = []
    for number in re.findall(r"[\w']+", line):
        numbers.append(int(number))
    return numbers

def findIfAlreadyAdded(x, y):
    global xIsInGraph, yIsInGraph
    xIsInGraph = graph.get(x)
    yIsInGraph = graph.get(y)

def setFriends(x, y):
    if(not xIsInGraph and not yIsInGraph):
        graph[x] = [[y], []]
        graph[y] = [[x], []]
    elif(xIsInGraph and not yIsInGraph):
        graph[y] = [graph[x][0][:], graph[x][1][:]]
        graph[y][0].append(x)
        graph[x][0].append(y)
    elif(yIsInGraph and not xIsInGraph):
        graph[x] = [graph[y][0][:], graph[y][1][:]]
        graph[y][0].append(x)
        graph[x][0].append(y)
    elif(areFriends(x, y) == 0):
        if(areEnemies(x, y) == 1):
            print(-1)
        else:
            visited.clear()
            traverseSetFriends(x, y)
            visited.clear()
            traverseSetFriends(y, x)
    visited.clear()
    regroupAllGraph()            
        
def setEnemies(x, y):
    if(not xIsInGraph and not yIsInGraph):
        graph[x] = [[], [y]]
        graph[y] = [[], [x]]
    elif(xIsInGraph and not yIsInGraph):
        graph[y] = [graph[x][1][:], graph[x][0][:]]
        graph[y][1].append(x)
        graph[x][1].append(y)
    elif(yIsInGraph and not xIsInGraph):
        graph[x] = [graph[y][1][:], graph[y][0][:]]
        graph[y][1].append(x)
        graph[x][1].append(y)
    elif(areEnemies(x, y) == 0):
        if(areFriends(x, y) == 1):
            print(-1)
        else:
            visited.clear()
            traverseSetEnemies(x, y)
            visited.clear()
            traverseSetEnemies(y, x)
    visited.clear()
    regroupAllGraph()        
    

def regroupAllGraph():
    for key in graph:
        if(key not in visited):
            visited.append(key)
            for friendA in graph[key][0]:
                for friendB in graph[key][0]:
                    if(friendA != friendB):
                        traverseSetFriends(friendA, friendB)
                for enemie in graph[key][1]:
                    traverseSetEnemies(friendA, enemie)

def traverseSetFriends(node, setNode):
    if(node not in visited):
        visited.append(node)
        for friend in graph[node][0]:
            if((friend != setNode) and (friend not in graph[setNode][0])):
                graph[setNode][0].append(friend)
        for enemie in graph[node][1]:
            if((enemie != setNode) and (enemie not in graph[setNode][1])):
                graph[setNode][1].append(enemie)
        for child in graph[node][0]:
            traverseSetFriends(child, setNode)

def traverseSetEnemies(node, setNode):
    if(node not in visited):
        visited.append(node)
        for enemie in graph[node][0]:
            if((enemie != setNode) and (enemie not in graph[setNode][1])):
                graph[setNode][1].append(enemie)
        for friend in graph[node][1]:
            if((friend != setNode) and (friend not in graph[setNode][0])):
                graph[setNode][0].append(friend)
        for child in graph[node][0]:
            traverseSetEnemies(child, setNode)

def areFriends(x, y):
    if(not xIsInGraph or not yIsInGraph):
        return 0
    else:
        visited.clear()
        areFriends = traverseFriends(x, y)
        if(not areFriends):
            visited.clear()
            areFriends = traverseFriends(y, x)
        if(areFriends):
            return areFriends
        else: 
            return 0

def traverseFriends(node, find):
    if(node not in visited):
        #print("node compare", node, node == find)
        if(node == find):
            return 1
        visited.append(node)
        for child in graph[node][0]:
            if(traverseFriends(child, find) == 1):
                return 1

def areEnemies(x, y):
    if(not xIsInGraph or not yIsInGraph):
        return 0
    else:
        visited.clear()
        enemies = traverseEnemies(x, y)
        if( not enemies):
            visited.clear()
            enemies = traverseEnemies(y, x)
        if(enemies):
            return enemies
        else: 
            return 0

def traverseEnemies(node, find):
    if(node not in visited):
        #print("node compare", node, graph[node][1])
        if(find in graph[node][1]):
            return 1
        visited.append(node)
        for child in graph[node][0]:
            if(traverseEnemies(child, find) == 1):
                return 1


for line in testFile:
    numbers = getNumbers(line)
    if(numbers):
        if(len(numbers) == 1):
            print("=================== STARTING NEW COUNT ==================")
        elif(numbers[0] > 0 and numbers[1] != numbers[2]):
            findIfAlreadyAdded(numbers[1], numbers[2])
            #print("Line:", numbers)
            if(numbers[0] == 1):
                setFriends(numbers[1], numbers[2])
            elif(numbers[0] == 2):
                setEnemies(numbers[1], numbers[2])
            elif(numbers[0] == 3):
                print(areFriends(numbers[1], numbers[2]))
            elif(numbers[0] == 4):
                print(areEnemies(numbers[1], numbers[2]))
        elif(numbers[0] == 0 ):
            print(graph)
            graph = {}
        








