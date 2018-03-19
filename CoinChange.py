class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        count = 0
        print("amount:" + str(amount) + "\ncoinset:" + str(coins))
        if len(coins) == 0:
            if amount == 0:
                return 1
            else:
                return 0
        if len(coins) == 1:
            if amount % coins[0] == 0 and amount / coins[0] < 500:
                return 1
            else:
                return 0
        else:
            maxcoin = max(coins)
            nextcoins = coins[:]
            nextcoins.remove(maxcoin)
            for i in range(0, amount // maxcoin + 1, 1):
                # print(str(i)+"*"+str(maxcoin))
                count = count + self.change(amount - i * maxcoin, nextcoins)
                print(count)
        return count


solution = Solution()
print(solution.change(10, [5, 2, 1]))
