"""There is a room with n lights which are turned on initially and 4 buttons on the wall. After performing exactly m unknown operations towards buttons, you need to return how many different kinds of status of the n lights could be.Suppose n lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:Flip all the lights.Flip lights with even numbers.Flip lights with odd numbers.Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...Example 1:Input: n = 1, m = 1.Output: 2Explanation: Status can be: [on], [off]Example 2:Input: n = 2, m = 1.Output: 3Explanation: Status can be: [on, off], [off, on], [off, off]Example 3:Input: n = 3, m = 1.Output: 4Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on]."""import timedef flipLights(n, m):    """    :type n: int    :type m: int    :rtype: int    """    if n > 4:        n = 4    if m > 4 and m % 2 == 0: m = 4    if m > 4 and m % 2 == 1: m = 3    statusSet = []    for s1 in range(0, m + 1):        for s2 in range(0, m + 1 - s1):            for s3 in range(0, m + 1 - s1 - s2):                lights = [1] * n                s4 = m - s1 - s2 - s3                lights = [(s1 & 1) ^ i for i in lights]                lights[1:n:2] = [(s2 & 1) ^ i for i in lights[1:n:2]]                lights[0:n:2] = [(s3 & 1) ^ i for i in lights[0:n:2]]                lights[0:n:3] = [(s4 & 1) ^ i for i in lights[0:n:3]]                if lights not in statusSet:                    statusSet.append(lights)                if len(statusSet) == 8:                    print(statusSet)                    return 8    return len(statusSet)start = time.time()print(flipLights(4, 3))print(flipLights(4, 1000))print(time.time() - start)