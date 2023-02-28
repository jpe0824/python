import time
import math
import random
import csv

counter = 0
actualBasicOps = []
elapsedTimes = []
array1 = [random.randint(0,1000) for i in range(10)]
array2 = [random.randint(0,1000) for i in range(100)]
array3 = [random.randint(0,1000) for i in range(250)]
array4 = [random.randint(0,1000) for i in range(500)]


nTimes = [array1, array2, array3, array4]

def partition(array, low, high):
    global counter
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        counter += 1
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quickSort(array, low, high):
    global counter
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def mergeSort(a):
    n = len(a)
    if n > 1:
        m = n // 2
        b = a[:m]
        c = a[m:]
        mergeSort(b)
        mergeSort(c)
        merge(a, b, c)

def merge(a, b, c):
    global counter
    i = j = k = 0
    n = len(b) + len(c)
    m = len(b)
    while j < m and k < n - m:
        if b[j] <= c[k]:
            a[i] = b[j]
            j += 1
        else:
            a[i] = c[k]
            k += 1
        i += 1
        counter += 1
    if j < m:
        a[i:n] = b[j:m]
    else:
        a[i:n] = c[k:n - m]

def runRecurs(func):
    global elapsedTimes
    global counter
    global actualBasicOps
    global nTimes
    elapsedTimes = []
    counter = 0
    actualBasicOps = []

    for n in nTimes:
        counter = 0
        t = time.perf_counter()
        print(func.__name__)
        if(func.__name__ == 'mergeSort'):
            funcName = func(n)
        else:
            funcName = func(n, 0, len(n) - 1)
        timeDelta = time.perf_counter() - t
        actualBasicOps.append(counter)
        elapsedTimes.append(timeDelta)
        print(f"(array length {len(n)}) in (calculated in {counter}) basicOps in {timeDelta}")

def printData(nTimes, actualBasicOps, elapsedTimes, func):
    print(f"Data for {func.__name__} function:")
    c = 0 #constant we're trying to ascertain
    sumOfItems = 0.0
    sumOfItemsSquared = 0.0
    sumOfItems2PowN = 0.0
    sumOfLogItems = 0.0
    sumOfNlogN = 0.0
    sumOfTimes = 0.0
    sumOfItemsGolden = 0.0
    estCsvData = []
    actualCsvData = []
    basicCsvData = []

    # do calculations
    i = 0
    for n in nTimes:
        ln = len(n)
        elapsedTime = elapsedTimes[i]
        sumOfItems += ln
        sumOfTimes += elapsedTime
        sumOfLogItems += math.log2(ln)
        sumOfNlogN += ln * math.log2(ln)
        sumOfItemsSquared += ln ** 2
        sumOfItemsGolden += math.pow(1.6, ln)
        sumOfItems2PowN += 2 ** ln
        i += 1

    c = sumOfTimes / sumOfItems
    cLgN = sumOfTimes / sumOfLogItems
    cNlgN = sumOfTimes / sumOfNlogN
    cSq = sumOfTimes / sumOfItemsSquared
    cGolden = sumOfTimes / sumOfItemsGolden
    c2PowN = sumOfTimes / sumOfItems2PowN
    header_est_times = ['n', 'c', 'cGolden', 'estimatedCNlgN', 'estimatedTimeLgN', 'estimatedTimeN', 'estimatedTimeNSq', 'estimated1.6^n', 'estimated2^n']
    header_n_basic_ops = ['n', 'basicOps']
    header_n_run_times = ['n', 'actualTimes']
    i = 0
    for n in nTimes:
        elapsedTime  = elapsedTimes[i]
        basicOperationCount = actualBasicOps[i]
        estimatedTime = c * basicOperationCount
        estimatedTimeNSq = cSq * basicOperationCount
        estimatedLgN = cLgN * basicOperationCount
        estimatedCNlgN = cNlgN * basicOperationCount
        estimatedGolden = cGolden * basicOperationCount
        estimated2PowN = c2PowN * basicOperationCount
        estData = [len(n), c, cGolden, estimatedCNlgN, estimatedLgN, estimatedTime, estimatedTimeNSq, estimatedGolden, estimated2PowN]
        basicOpsData = [len(n), basicOperationCount]
        actualData = [len(n), elapsedTime]
        estCsvData.append(estData)
        basicCsvData.append(basicOpsData)
        actualCsvData.append(actualData)
        i += 1
    with open(f'{func.__name__}.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header_est_times)
        writer.writerows(estCsvData)
        writer.writerow(header_n_basic_ops)
        writer.writerows(basicCsvData)
        writer.writerow(header_n_run_times)
        writer.writerows(actualCsvData)

def main():
    global elapsedTimes
    global actualBasicOps
    global nTimes
    runRecurs(mergeSort)
    printData(nTimes, actualBasicOps, elapsedTimes, mergeSort)
    runRecurs(quickSort)
    printData(nTimes, actualBasicOps, elapsedTimes, quickSort)

if __name__ == "__main__":
    main()