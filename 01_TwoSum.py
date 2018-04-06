class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, n in enumerate(nums):
            res = target - n
            if res in dic:
                return [i, dic[res]]
            else:
                dic[n] = i
