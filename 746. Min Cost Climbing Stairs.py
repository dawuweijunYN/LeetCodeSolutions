"""On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.Example 1:Input: cost = [10, 15, 20]Output: 15Explanation: Cheapest is start on cost[1], pay that cost and go to the top.Example 2:Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]Output: 6Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].Note:cost will have a length in the range [2, 1000].Every cost[i] will be an integer in the range [0, 999]."""class Solution:    def minCostClimbingStairs(self, cost):        """        :type cost: List[int]        :rtype: int        """        if not cost or len(cost)==0: return 0        if len(cost)==1: return cost[0]        if len(cost)==2: return min(cost)        l1=cost[0]        l2=cost[1]        for i in cost[2:]:            temp=l1            l1=l2            l2=i+min(temp,l1)        # return min(self.minCostClimbingStairs(cost[1:])+cost[0],self.minCostClimbingStairs(cost[2:])+cost[1])        return min(l1,l2)        