def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    lst=range(2,n)
    for i in lst:
        for j in lst[i:]:
            if lst[j]%


a=[1,2,3]
a.remove(2)
print(a.index(3))
