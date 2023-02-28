import time
import math
counter = 0
actualBasicOperations = []
elapsedTimes = []
nTimes = [10, 15, 20]
def fibonacci_recursive(n):
    global counter
    if (n == 1):
        return 1
    if (n == 0):
        return 0
    else:
        counter += 1  # basic ops is addition of two recursive calls
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def runRecurs():
    global elapsedTimes
    global counter
    global actualBasicOperations
    global nTimes
    for n in nTimes:
        counter = 0
        t = time.perf_counter()
        fibOfN = str(fibonacci_recursive(n))
        timeDelta = time.perf_counter() - t
        actualBasicOperations.append(counter)
        elapsedTimes.append(timeDelta)
        print(f"({n}) = {fibOfN} (calculated in {counter}) basicOps in {timeDelta}")

def printData(nTimes, actualBasicOperations, elapsedTimes):
    averageTime = 0
    c = 0 #constant we're trying to ascertain
    sumOfItems = 0.0
    sumOfItemsSquared = 0.0
    sumOfItems2PowN = 0.0
    sumOfLogItems = 0.0
    sumOfTimes = 0.0
    sumOfItemsGolden = 0.0

    # do calculations
    i = 0
    for n in nTimes:
        elapsedTime = elapsedTimes[i]
        print(f"n:  {n}, elapsedTime:  {elapsedTime}")
        sumOfItems += n
        sumOfTimes += elapsedTime
        sumOfLogItems += math.log2(n)
        sumOfItemsSquared += n ** 2
        sumOfItemsGolden += math.pow(1.6, n)
        sumOfItems2PowN += 2 ** n
        i += 1

    c = sumOfTimes / sumOfItems
    cLgN = sumOfTimes / sumOfLogItems
    cSq = sumOfTimes / sumOfItemsSquared
    cGolden = sumOfTimes / sumOfItemsGolden
    c2PowN = sumOfTimes / sumOfItems2PowN
    #print(f"c: {c}")
    #print(f"total items: {sumOfItems}, total time: {sumOfTimes}, averageTimePerRecord: {c}\n")
    #print headers
    nTimesHeader = "n"
    basicOps = "basicOps"
    cHeader = "c"
    goldenHeader = "cGolden"
    estimatedTimeLgN = "estimatedTimeLgN"
    estHeader = "estimatedTimeN"
    estimatedTimeNSq = "estimatedTimeNSq"
    estimatedTimeGolden = "estimated1.6^n"
    estimatedTime2PowN = "estimated2^n"
    actualHeader = "actualTime"
    print(f"{nTimesHeader:>25} {basicOps:>25} {cHeader:>25} {goldenHeader:>25} {estimatedTimeLgN:>25} {estHeader:>25} {estimatedTimeNSq:>25} {estimatedTimeGolden:>25} {estimatedTime2PowN:>25} {actualHeader:>25}")
    i = 0
    for n in nTimes:
        elapsedTime  = elapsedTimes[i]
        basicOperationCount = actualBasicOperations[i]
        estimatedTime = c * basicOperationCount
        estimatedTimeNSq = cSq * basicOperationCount
        estimatedLgN = cLgN * basicOperationCount
        estimatedGolden = cGolden * basicOperationCount
        estimated2PowN = c2PowN * basicOperationCount
        print(f"{n:>25} {basicOperationCount:>25} {c:>25} {cGolden:>25} {estimatedLgN:>25} {estimatedTime:>25} {estimatedTimeNSq:>25} {estimatedGolden:>25} {estimated2PowN:>25} {elapsedTime:>25}")
        i += 1

def main():
    global elapsedTimes
    global actualBasicOperations
    global nTimes
    runRecurs()
    printData(nTimes, actualBasicOperations, elapsedTimes)

if __name__ == "__main__":
    main()
