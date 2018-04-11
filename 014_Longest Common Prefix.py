"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortStr=self.shortestString(strs)
        if shortStr=="":return ""
        else:
            res = ""
            for i in range(len(shortStr)):
                for j in strs:
                    if j[i]!=shortStr[i]:return res
                res=res+shortStr[i]
            return res

    def shortestString(self,strs):
        if strs == []: return ""
        else:
            res = strs[0]
            minLen = len(res)
            for i in strs:
                if len(i)<minLen:
                    res=i
                    minLen=len(i)
            return res

solution=Solution()
a=['12','1222','1222']
print(solution.longestCommonPrefix(a))