import random
import time

original_values = []
for x in range(5100):
    original_values.append(random.randint(1, 100_000))

def bubleSort():
    values =  original_values.copy()
    for i in range(len(values)):
        k = 0
        while k + i + 1 < len(values):
            if(values[k] > values[k+1]):
                temp = values[k]
                values[k] = values[k+1]
                values[k+1] = temp
            k = k + 1

    #print("Buble Sort")
    #print(original_values)
    #print(values)

def insertionSort():
    values =  original_values.copy()
    for i in range(len(values)-1):
        if(values[i] > values[i+1]):
            j = i + 1
            while j > 0 and values[j] < values[j-1]:
                temp = values[j]
                values[j] = values[j-1]
                values[j-1] = temp
                j = j - 1       

    #print("Insetion Sort")
    #print(original_values)
    #print(values)

def recursiveQuickSort(values, leftP, rightP):
    #print("Recursion", leftP, rightP)
    if(leftP < rightP and rightP - leftP > 1):
        goLeft = False
        swap = False
        left = leftP
        right = rightP
        while left < right:
            if(values[left] > values[right]):
                temp =  values[left]
                values[left] = values[right]
                values[right] = temp
                goLeft = not goLeft
                swap = True
            else:
                if(goLeft):
                    right = right -1
                else:
                    left = left +1
        #print(leftP, rightP, left, right)
        if(not swap and left == rightP):
            left = left - 1

        recursiveQuickSort(values, leftP, left)
        recursiveQuickSort(values, left, rightP)
                
def quickSort():
    values =  original_values.copy()
    #values = [27, 5, 56, 35, 16, 60, 15, 77, 59, 3, 33, 40, 6]
    recursiveQuickSort(values, 0, len(values)-1)
    #print("Quick Sort")
    #print(original_values)
    #print(values)

def mergeSort():
    values = original_values.copy()
    lists = []
    i = 0
    #print(values)
    while i < len(values):
        if(i == len(values) -1 ):
            lists.append([values[i]])
        elif(values[i] < values[i+1]):
            lists.append([values[i], values[i+1]])
        else:
            lists.append([values[i+1], values[i]])
        i = i + 2 
    i = 0
    while len(lists) > 1:
        if(i >= len(lists) - 2):
            i = 0
        lists.insert(i, mergeLists(lists.pop(i), lists.pop(i)))
        i = i+1
    #print(original_values, "\n")
    #print(len(lists[0]), lists)
    
def mergeLists(list1, list2):
    result = []
    #print("Lists:", list1, list2)
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    if(len(list1) > 0):
        result.extend(list1)
    elif(len(list2) > 0):
        result.extend(list2)
    #print("Results:", result)
    return result

def heapSort():
    values = original_values.copy()
    #values = [27, 5, 56, 35, 16, 60, 15, 77, 59, 3, 33, 40, 6]
    #print(values)
    values = orderHeap(values)
    result = []
    while len(values) > 1:
        result.append(values[0])
        values[0] = values[len(values) -1]
        values = orderHeap(values[:len(values)-1])
    result.append(values[0])
    #print(values, result)

def orderHeap(values):
    isSwap = True
    length = len(values)
    while isSwap:
        isSwap = False
        i = 0
        j = 1
        if(j >= length):
            break
        if(values[i] > values[j]):
            isSwap = True
            temp = values[i]
            values[i] = values[j]
            values[j] = temp
        if(j+1 < length and values[i] > values[j+1]):
            isSwap = True
            temp = values[i]
            values[i] = values[j+1]
            values[j+1] = temp
        j = j+2
        i = i+1
    return values

def bucketSort():
    values = original_values.copy()
    buckets = {
        '0' : [], '1' : [], '2' : [], '3' : [], '4' : [],
        '5' : [], '6' : [], '7' : [], '8' : [], '9' : []
    }

    maxNumber = 0
    for i in range(len(values)):
        if(values[i] > maxNumber):
            maxNumber = values[i]

    maxDigits = len(str(maxNumber))

    for i in range(len(values)):
        values[i] = str(values[i])
        if(len(values[i]) < maxDigits):
            values[i] = '0'*(maxDigits - len(values[i])) + values[i]

    for i in range(maxDigits):
        for value in values:
            digitPosition = value[len(value) - i -1]
            buckets.get(digitPosition).append(value)
        
        values.clear()
        for key in buckets:
            array = buckets.get(key)
            for i in range(len(array)):
                values.append(array.pop(0))

    #print(original_values)
    #print(values)
    #print(buckets)


start = time.time()
bubleSort()
end = time.time()
print("Buble Sort: Time=", end - start)

start = time.time()
insertionSort()
end = time.time()
print("Insertion Sort: Time=", end - start)

start = time.time()
quickSort()
end = time.time()
print("Quick Sort: Time=", end - start)

start = time.time()
mergeSort()
end = time.time()
print("Merge Sort: Time=", end - start)

start = time.time()
heapSort()
end = time.time()
print("Heap Sort: Time=", end - start)

start = time.time()
bucketSort()
end = time.time()
print("Bucket Sort: Time=", end - start)