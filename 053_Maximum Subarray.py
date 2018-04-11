"""Find the contiguous subarray within an array (containing at least one number) which has the largest sum.For example, given the array [-2,1,-3,4,-1,2,1,-5,4],the contiguous subarray [4,-1,2,1] has the largest sum = 6.More practice:If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""class Solution(object):    def maxSubArray(self, nums):        """        :type nums: List[int]        :rtype: int        """        maxTemp=nums[0]        maxAll=nums[0]        for i in nums[1:]:            maxTemp=max(maxTemp+i,i)            maxAll=max(maxTemp,maxAll)        return maxAll