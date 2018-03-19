
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    reversedNum = 0
    while(reversedNum<x):
        reversedNum=reversedNum*10+x%10
        xtemp = x
        x=int(x/10)
    if reversedNum == x or reversedNum == xtemp:
        return True
    return False

print(isPalindrome(12213))