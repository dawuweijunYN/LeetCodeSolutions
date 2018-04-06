class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i, j in enumerate(zip(*strs)):
            print(i,j)
            print(set(j))
            if len(set(j))>1:
                return strs[0][:i]


solution=Solution()
a=['121','1222','1222']

print(solution.longestCommonPrefix(a))