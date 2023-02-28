
import time
import math
from test import printData
counter = 0
elapsedTimes = []
actualBasicOperations = []
nTimes = [10, 15, 20]
def fibonacci_dp(n):
    global counter
    fibSequence = [ 0, 1 ]

    for i in range(2, n + 1):
        counter += 1
        fibSequence.append(fibSequence[i-1] + fibSequence[i-2])

    return fibSequence[n]

def run_dp():
    global elapsedTimes
    global nTimes
    global counter
    global actualBasicOperations
    fibSeqDp = ""
    i = 0
    for n in nTimes:
        counter = 0
        if (len(fibSeqDp) > 0):
            fibSeqDp += ', '
        t = time.perf_counter()
        fibOfN = fibonacci_dp(n)
        timeDelta = time.perf_counter() - t
        fibSeqDp += str(fibOfN)
        actualBasicOperations.append(counter)
        elapsedTimes.append(timeDelta)
    print(fibSeqDp)
def main():
    global elapsedTimes
    global actualBasicOperations
    global nTimes
    run_dp()
    printData(nTimes, actualBasicOperations, elapsedTimes)

if __name__ == "__main__":
    main()
