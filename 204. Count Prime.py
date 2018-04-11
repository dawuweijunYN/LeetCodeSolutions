"""
Description:

Count the number of prime numbers less than a non-negative number, n.
"""
import time


def findPrime(n):
    res = list(range(2, n + 1))
    for i in res:
        if i != 0:
            for j in range(i * 2 - 2, n + 1 - 2, i):
                res[j] = 0
    return [i for i in res if i != 0]


def findPrime2(n):
    res = list(range(2, n))
    for i in res:
        for j in range(i * 2, n, i):
            if j in res:
                res.remove(j)
    return res


def findPrime3(n):
    res = [True] * n
    if n < 3: return 0
    res[0] = False
    res[1] = False
    for i in range(n):
        if res[i]:
            for j in range(i * 2, n, i):
                res[j] = False
    return [i for i in range(n) if res[i]]


start = time.time()
print(findPrime3(499979))
print(time.time() - start)
